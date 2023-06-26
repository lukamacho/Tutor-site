import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';

export default function StudentMessages() {
  const location = useLocation();
  const email = location.state?.email;

  const [messagedStudents, setMessagedStudents] = useState([]);

  useEffect(() => {
    const fetchMessagedStudents = async () => {
      try {
        const response = await fetch(`http://localhost:8000/tutor/messaged_students/${email}`);
        const data = await response.json();
        setMessagedStudents(data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchMessagedStudents();
  }, [email]);

  return (
    <div>
      <h1>Tutor Messages</h1>
      <p>Email: {email}</p>
      <h2>Messaged Tutors:</h2>
      {messagedStudents.length === 0 ? (
        <p>No messages</p>
      ) : (
        <ul>
          {messagedStudents.map((student) => (
            <li key={student.id}>{student}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
