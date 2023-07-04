import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';

export default function StudentMessages() {
  const location = useLocation();
  const email = location.state?.email;

  const [messagedStudents, setMessagedStudents] = useState([]);
  const [receiverMail, setReceiverMail] = useState(null);
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState([]);
  const [meetingDate, setMeetingDate] = useState('');
  const [meetingTime, setMeetingTime] = useState('');
  const [meetingLink, setMeetingLink] = useState('');

  useEffect(() => {
    const fetchMessagedTutors = async () => {
      try {
        const response = await fetch(`http://localhost:8000/tutor/messaged_students/${email}`);
        const data = await response.json();
        if (data.length > 0) {
          setMessagedStudents(data);
          setReceiverMail(data[0]);
        } else {
          setMessagedStudents([]);
          setReceiverMail(null);
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
      setMessage('');

      const updatedResponse = await fetch(`http://localhost:8000/tutor/messages/${email}/${receiverMail}`);
      const updatedData = await updatedResponse.json();
      setMessages(updatedData);
    } catch (error) {
      console.error(error);
    }
  };

  const handleGenerateMeetingLink = async () => {
      const date = new Date(meetingDate);

      // Extract hours and minutes from meetingTime
      const [hours, minutes] = meetingTime.split(':').map(Number);

      // Create new Date object with correct time
      const dateTime = new Date(date.getFullYear(), date.getMonth(), date.getDate(), hours, minutes);
      console.log(dateTime.toISOString())
      const requestData = {
        tutor_mail: email,
        student_mail: receiverMail,
        date_and_time: dateTime.toISOString(),
      };

      try {
        const response = await fetch('http://localhost:8000/generate_meeting_link', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(requestData),
        });

        const data = await response.json();
        setMeetingLink(data.meeting_link);
      } catch (error) {
        console.error(error);
      }
    };



  const handleStudentClick = (student) => {
    setReceiverMail(student);
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
        <h2>Generate Meeting Link:</h2>
        <input
          type="date"
          value={meetingDate}
          onChange={(e) => setMeetingDate(e.target.value)}
          placeholder="Meeting Date"
        />
        <input
          type="time"
          value={meetingTime}
          onChange={(e) => setMeetingTime(e.target.value)}
          placeholder="Meeting Time"
        />
        <button onClick={handleGenerateMeetingLink}>Generate Meeting Link</button>
        {meetingLink && <p>Meeting Link: {meetingLink}</p>}
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
