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
    <div style={containerStyle}>
      <ThemeProvider theme={theme}>
        <HeaderStyledTypography variant="h4" align="center">
          Student's Messages
        </HeaderStyledTypography>
        <ListBox>
          <Typography variant="h4" sx={{ fontWeight: 'bold' }}>
            Messaged Tutors:
          </Typography>
          {messagedTutors.length === 0 ? (
            <Typography variant="h5" sx={{ marginLeft: 1, }}>
              No Messages!
            </Typography>
          ) : (
            <List>
              {messagedTutors.map((tutor, index) => (
                <ListItem key={index} onClick={() => handleTutorClick(tutor)}>
                  {tutor}
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