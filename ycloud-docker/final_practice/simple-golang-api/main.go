package main
//
import (
    "database/sql"
    "encoding/json"
    "fmt"
    "log"
    "net/http"
    "os"
    _ "github.com/lib/pq" 
)

var (
    host     = os.Getenv("API_DB_HOST")
    port     = os.Getenv("API_DB_PORT")
    user     = os.Getenv("API_DB_USER")
    password = os.Getenv("API_DB_PASS")
    dbname   = os.Getenv("API_DB_NAME")
)

var db *sql.DB

type Response struct {
    Message   string `json:"message"`
    PGVersion string `json:"postgres_version"`
}

func main() {
    pgConnStr := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable", host, port, user, password, dbname)

    conn, err := sql.Open("postgres", pgConnStr)
    if err != nil {
        log.Fatalf("Error opening database connection: %v", err)
    }
    db = conn
    defer db.Close()

    err = db.Ping()
    if err != nil {
        log.Fatalf("Error connecting to the database: %v", err)
    }
    fmt.Println("Connected to the PostgreSQL database")

    http.HandleFunc("/", HelloServer)

    fmt.Println("Server is listening on port 8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}

func HelloServer(w http.ResponseWriter, r *http.Request) {
    rows, err := db.Query("SELECT 'Hello world', version();")
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
    defer rows.Close()

    var responses []Response

    for rows.Next() {
        var response Response
        err := rows.Scan(&response.Message, &response.PGVersion)
        if err != nil {
            http.Error(w, err.Error(), http.StatusInternalServerError)
            return
        }
        responses = append(responses, response)
    }

    json.NewEncoder(w).Encode(responses)
}