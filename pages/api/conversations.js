import sqlite3 from 'sqlite3';

export default function handler(req, res) {
  const db = new sqlite3.Database('conversations.db');
  db.all('SELECT * FROM conversations', [], (err, rows) => {
    if (err) {
      res.status(500).json({ error: err.message });
      return;
    }
    res.status(200).json({ conversations: rows });
  });
  db.close();
} 