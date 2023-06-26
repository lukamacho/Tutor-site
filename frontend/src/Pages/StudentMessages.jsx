import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';

export default function StudentMessages() {
  const location = useLocation();
  const email = location.state?.email;

  const [messagedTutors, setMessagedTutors] = useState([]);
  const [receiverMail, setReceiverMail] = useState(null); // Initialize receiverMail as null
  const [message, setMessage] = useState(''); // Track the input message
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const fetchMessagedTutors = async () => {
      try {
        const response = await fetch(`http://localhost:8000/student/messaged_tutors/${email}`);
        const data = await response.json();
        console.log(data);
        if (data.length > 0) {
          setMessagedTutors(data);
          setReceiverMail(data[0]); // Set the initial receiver tutor as the first tutor in the list
        } else {
          setMessagedTutors([]);
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
          const response = await fetch(`http://localhost:8000/student/messages/${email}/${receiverMail}`);
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
      tutor_mail: receiverMail,
      student_mail: email,
    };
    try {
      const response = await fetch('http://localhost:8000/student/message_to_tutor', {
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
      const updatedResponse = await fetch(`http://localhost:8000/student/messages/${email}/${receiverMail}`);
      const updatedData = await updatedResponse.json();
      console.log(updatedData);
      setMessages(updatedData);
    } catch (error) {
      console.error(error);
    }
  };

  const handleTutorClick = (tutor) => {
    setReceiverMail(tutor); // Update the receiver tutor when a tutor is clicked
  };

  return (
    <div>
      <h1>Student Messages</h1>
      <p>Email: {email}</p>
      <h2>Messaged Tutors:</h2>
      {messagedTutors.length === 0 ? (
        <p>No messages</p>
      ) : (
        <ul>
          {messagedTutors.map((tutor, index) => (
            <li key={index} onClick={() => handleTutorClick(tutor)}>
              {tutor}
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
