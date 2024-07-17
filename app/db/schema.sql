CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT NOT NULL,
    label TEXT NOT NULL,
    local_path TEXT NOT NULL,
    device_name TEXT NOT NULL,
    remote_path TEXT NOT NULL
);
