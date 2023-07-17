import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import backgroundImage from '../Images/MessagesBG.png';
import { theme } from "../Components/Theme"
import { ThemeProvider } from '@mui/material/styles';
import { HeaderStyledTypography } from "../Components/Styles"
import { styled } from '@mui/system';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

const containerStyle = {
  backgroundImage: `url(${backgroundImage})`,
  backgroundSize: 'cover',
  backgroundRepeat: 'repeat',
  backgroundPosition: 'center',
  minHeight: '100vh',
};

export const ListBox = styled(Box)(({ theme }) => ({
  alignItems: 'center',
  backgroundColor: 'rgba(255, 255, 255, 0.5)',
  borderRadius: '14px',
  display: 'flex',
  flexDirection: 'row',
  height: 'auto',
  justifyContent: 'center',
  margin: 'auto',
  marginTop: 20,
  width: "90%",
  padding: 25,
}));

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
    <div style={containerStyle}>
      <ThemeProvider theme={theme}>
        <HeaderStyledTypography variant="h4" align="center">
          Tutor's Messages
        </HeaderStyledTypography>
        <ListBox>
          <Typography variant="h4" sx={{ fontWeight: 'bold' }}>
            Messaged Students:
          </Typography>
          {messagedStudents.length === 0 ? (
            <Typography variant="h5" sx={{ marginLeft: 1, }}>
              No Messages!
            </Typography>
          ) : (
            <List>
              {messagedStudents.map((student, index) => (
                <ListItem key={index} onClick={() => handleStudentClick(student)}>
                  {student}
                </ListItem>
              ))}
            </List>
          )}
        </ListBox>
        <ListBox>
          {receiverMail &&
            <div>
              <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                Receiver Mail:
              </Typography>
              <Typography variant="h6" sx={{ marginLeft: 1, }}>
                {receiverMail}
              </Typography>
            </div>}
          <TextField
            id="message"
            fullWidth
            label="Enter Your Message"
            name="message"
            onChange={e => setMessage(e.target.value)}
            value={message}
            size="small"
          />
          <Button
            onClick={handleSendMessage}
            sx={{ marginLeft: 1, }}
            variant="outlined"
            size="small"
          >
            Send
          </Button>
        </ListBox>
        <ListBox>
          <Typography variant="h4" sx={{ fontWeight: 'bold' }}>
            Generate Meeting Link:
          </Typography>
          <TextField
            type="date"
            id="meeting-date"
            fullWidth
            name="meeting-date"
            onChange={e => setMeetingDate(e.target.value)}
            value={meetingDate}
            size="small"
          />
          <Button
            onClick={handleGenerateMeetingLink}
            sx={{ marginLeft: 1, }}
            variant="outlined"
            size="small"
          >
            Generate
          </Button>
          {meetingLink &&
            <div>
              <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                Meeting Link:
              </Typography>
              <Typography variant="h6" sx={{ marginLeft: 1, }}>
                {meetingLink}
              </Typography>
            </div>}
        </ListBox>
        <ListBox>
          <Typography variant="h4" sx={{ fontWeight: 'bold' }}>
            Messages:
          </Typography>
          {messages.length === 0 ? (
            <Typography variant="h5" sx={{ marginLeft: 1, }}>
              No Messages!
            </Typography>
          ) : (
            <List>
              {messages.map((message, index) => (
                <ListItem key={index}>
                  <Typography variant="h6" sx={{ marginLeft: 1, }}>
                    {message.message_text}
                  </Typography>
                </ListItem>
              ))}
            </List>
          )}
        </ListBox>
      </ThemeProvider>
    </div>
  );
}