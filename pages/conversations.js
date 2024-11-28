import { useEffect, useState } from 'react';

export default function Conversations() {
  const [conversations, setConversations] = useState([]);

  useEffect(() => {
    fetch('/api/conversations')
      .then((res) => res.json())
      .then((data) => setConversations(data.conversations));
  }, []);

  return (
    <div>
      <h1>Conversations</h1>
      <ul>
        {conversations.map((conv) => (
          <li key={conv.user}>
            <strong>User:</strong> {conv.user}
            <br />
            <strong>Last Message:</strong> {conv.last_message}
          </li>
        ))}
      </ul>
    </div>
  );
} 