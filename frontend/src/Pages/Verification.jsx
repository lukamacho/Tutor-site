import backgroundImage from '../Images/VerificationBG.png';
import { styled } from '@mui/system';
import Box from '@mui/material/Box';
import PropTypes from 'prop-types';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import { useState } from 'react';
import Button from '@mui/material/Button';
import { useLocation, useNavigate } from 'react-router-dom';

export const background = {
  backgroundImage: `url(${backgroundImage})`,
  backgroundSize: 'cover',
  backgroundRepeat: 'repeat',
  backgroundPosition: 'center',
  minHeight: '100vh',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
};

export const StyledBox = styled(Box)(({ theme }) => ({
  marginTop: -100,
  padding: 25,
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  borderRadius: '8px',
  boxShadow: '0.5px 0.5px 10px rgba(0, 0, 0, 0.2)',
  backgroundColor: 'rgba(255, 255, 255, 0.8)',
  justifyContent: 'center',
}));

const Verification = ({ setToken }) => {
  const location = useLocation();
  const navigate = useNavigate();

  const is_student = location.state?.is_student;
  const email = location.state?.email;
  const first_name = location.state?.first_name;
  const last_name = location.state?.last_name;
  const password = location.state?.password;

  const [verificationCode, setVerificationCode] = useState('');
  const [verificationError, setVerificationError] = useState(false);

  const handleVerification = async (e) => {
    e.preventDefault();

    const expectedCode = location.state?.verificationCode;
    if (verificationCode === expectedCode) {
      const data = {
        "first_name": first_name,
        "last_name": last_name,
        "mail": email,
        "password": password,
        "is_student": is_student,
      }

      try {
        const response = await fetch('http://localhost:8000/add_user', {
          method: 'POST',
          body: JSON.stringify(data),
          headers: { 'Content-Type': 'application/json' }
        });
        const result = await response.json();
      } catch (error) {
        console.error(error);
      }

      if (is_student) {
        navigate("/student_profile", {
          state: { email, first_name, last_name, password }
        });
      } else {
        navigate("/tutor_profile", {
          state: { email, first_name, last_name, password }
        });
      }
    } else {
      setVerificationError(true);
    }
  };

  return (
    <div style={background}>
      <StyledBox>
        <Typography component="h1" variant="h4" sx={{ m: 1.5 }}>
          Verification
        </Typography>
        <Typography component="h2" variant="h6" sx={{ m: 1.5 }}>
          Enter the verification code that was sent to your email below.
        </Typography>
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <TextField
            margin="normal"
            required
            label="Verification Code"
            autoFocus
            value={verificationCode}
            onChange={(e) => setVerificationCode(e.target.value)}
          />
          <Button
            variant="outlined"
            onClick={(e) => handleVerification()}
            sx={{ height: 40, }}
            size="large"
          >
            Verify
          </Button>
        </div>
        {verificationError && (
          <Typography
            style={{ marginTop: 8, }}
            variant="body1"
            color="error"
          >
            Incorrect verification code. Please try again.
          </Typography>
        )}
      </StyledBox>
    </div>
  );
}

Verification.propTypes = {
  setToken: PropTypes.func.isRequired,
};

export default Verification;