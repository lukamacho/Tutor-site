import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';

export default function StudentMessages() {
  const location = useLocation();
  const email = location.state?.email;

  const [messagedTutors, setMessagedTutors] = useState([]);

  useEffect(() => {
    const fetchMessagedTutors = async () => {
      try {
        const response = await fetch(`http://localhost:8000/student/messaged_tutors/${email}`);
        const data = await response.json();
        console.log(data);
        setMessagedTutors(data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchMessagedTutors();
  }, [email]);

  return (
    <div>
      <h1>Student Messages</h1>
      <p>Email: {email}</p>
      <h2>Messaged Tutors:</h2>
      {messagedTutors.length === 0 ? (
        <p>No messages</p>
      ) : (
        <ul>
          {messagedTutors.map((tutor) => (
            <li key={tutor.id}>{tutor}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
