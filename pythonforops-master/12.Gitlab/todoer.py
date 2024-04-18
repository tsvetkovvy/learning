import difflib
import os
import re
import git
import gitlab


COMMENT_RE = re.compile(r".*?#\s*?TODO:(.*)")


def check_on_todo(row: str):
    if matcher := re.search(COMMENT_RE, row):
        return matcher.group(1).strip()


def get_diff(change_types: list, ahead, stale):
    for change_type in change_types:
        for diff in stale.diff(ahead).iter_change_type(change_type):
            yield diff


def create_issue(project, todo, row, mr, line_no, new_path, old_path):
    for discussion in mr.discussions.list():
        for note in discussion.attributes["notes"]:
            if todo in note["body"] and not note["resolved"]:
                print("Discussion can not be duplicated")
                return

    issue = project.issues.create({'title': todo,
                                   'description': 'Created from TODO comment task'})
    discussion_content = f"[{project.name_with_namespace}]Из TODO была создана задача [{issue.iid}]({project.web_url + '/-/issues/' + str(issue.iid)})\n" \
                         f"```suggestion:-0+0\n{row} [{issue.iid}]\n```"

    mr_diff = mr.diffs.list()[0]
    mr.discussions.create({'body': discussion_content,
                          'position': {
                              'base_sha': mr_diff.base_commit_sha,
                              'start_sha': mr_diff.start_commit_sha,
                              'head_sha': mr_diff.head_commit_sha,
                              'position_type': 'text',
                              'new_line': line_no,
                              'old_path': old_path,
                              'new_path': new_path}
                          })


def main():
    gl = gitlab.Gitlab("https://gitlab.slurm.io", os.getenv("GITLAB_TOKEN"))
    project = gl.projects.get(os.getenv("CI_PROJECT_ID"))
    mr = project.mergerequests.get(os.getenv("CI_MERGE_REQUEST_IID"))
    repo_path = os.getcwd()
    repo = git.Repo(repo_path)

    origin = repo.remotes.origin

    origin.fetch()

    new_branch = repo.create_head("new_branch")
    repo.heads.new_branch.set_tracking_branch(origin.refs.new_branch)
    repo.git.checkout(new_branch)
    origin.pull()

    repo.index.add([os.path.join(repo_path, "todoer.py")])
    repo.index.add([os.path.join(repo_path, "app.py")])
    repo.index.commit("feat: add todoer project")

    origin.push(new_branch.name)

    for diff in get_diff(["A", "M"], repo.head.commit, origin.refs.master.commit):
        stale = "" if diff.a_blob is None else diff.a_blob.data_stream.read().decode("utf-8")
        ahead = "" if diff.b_blob is None else diff.b_blob.data_stream.read().decode("utf-8")

        line_no = 0
        for row in difflib.ndiff(stale.splitlines(), ahead.splitlines()):
            row = row.strip()
            if row == "":
                line_no += 1
                continue
            elif row[0] == "-":
                continue
    #             TODO: Реализовать удаление задач при удалении TODO
            elif row[0] == "+":
                line_no += 1
                row = row.strip("+ ")
                if todo := check_on_todo(row):
                    create_issue(project, todo, row, mr, line_no, diff.b_path, diff.a_path)


if __name__ == '__main__':
    main()
