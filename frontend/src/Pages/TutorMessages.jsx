import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';

export default function StudentMessages() {
  const location = useLocation();
  const email = location.state?.email;

  const [messagedStudents, setMessagedStudents] = useState([]);
  const [receiverMail, setReceiverMail] = useState(null); // Initialize receiverMail as null
  const [message, setMessage] = useState(''); // Track the input message
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const fetchMessagedTutors = async () => {
      try {
        const response = await fetch(`http://localhost:8000/tutor/messaged_students/${email}`);
        const data = await response.json();
        console.log(data);
        if (data.length > 0) {
          setMessagedStudents(data);
          setReceiverMail(data[0]); // Set the initial receiver tutor as the first tutor in the list
        } else {
          setMessagedStudents([]);
          setReceiverMail(null); // Reset receiver tutor if there are no messaged tutors
        }
      } catch (error) {
        console.error(error);
      }
    };

    fetchMessagedTutors();
  }, [email]);

  useEffect(() => {
    if (receiverMail) {
      const fetchMessages = async () => {
        try {
          const response = await fetch(`http://localhost:8000/tutor/messages/${email}/${receiverMail}`);
          const data = await response.json();
          console.log(data);
          setMessages(data);
        } catch (error) {
          console.error(error);
        }
      };

      fetchMessages();
    }
  }, [email, receiverMail]);

  const handleSendMessage = async () => {
    const messageData = {
      message_text: message,
      tutor_mail: email,
      student_mail: receiverMail,
    };
    try {
      const response = await fetch('http://localhost:8000/tutor/message_to_student', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(messageData),
      });
      const data = await response.json();
      console.log(data);
      setMessage('');

      // Fetch updated messages after sending the message
      const updatedResponse = await fetch(`http://localhost:8000/tutor/messages/${email}/${receiverMail}`);
      const updatedData = await updatedResponse.json();
      console.log(updatedData);
      setMessages(updatedData);
    } catch (error) {
      console.error(error);
    }
  };

  const handleStudentClick = (student) => {
    setReceiverMail(student); // Update the receiver tutor when a tutor is clicked
  };

  return (
    <div>
      <h1>Tutor Messages</h1>
      <p>Email: {email}</p>
      <h2>Messaged Students:</h2>
      {messagedStudents.length === 0 ? (
        <p>No messages</p>
      ) : (
        <ul>
          {messagedStudents.map((student, index) => (
            <li key={index} onClick={() => handleStudentClick(student)}>
              {student}
            </li>
          ))}
        </ul>
      )}
      {receiverMail && <p>Receiver Mail: {receiverMail}</p>}
      <div>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Enter your message"
        />
        <button onClick={handleSendMessage}>Send Message</button>
      </div>
      <div>
        <h2>Messages:</h2>
        {messages.length === 0 ? (
          <p>No messages</p>
        ) : (
          <ul>
            {messages.map((message, index) => (
              <li key={index}>{message.message_text}</li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
