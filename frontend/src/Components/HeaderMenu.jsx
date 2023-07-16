import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import Button from '@mui/material/Button';
import LightbulbIcon from '@mui/icons-material/Lightbulb';
import AccountController from './AccountController';
import { HeaderTypography } from "./Styles"
import PropTypes from 'prop-types';
import { useEffect, useState } from 'react';

const HeaderMenu = ({ token }) => {
  const [isUser, setIsUser] = useState(false);

  useEffect(() => {
    const handleVerification = async () => {
      let emailToken = JSON.parse(sessionStorage.getItem('email'))
      let emailStr = emailToken === null ? '' : emailToken

      const data = {
        token: token,
        email: emailStr,
      }

      console.log("/verify_token/parameters")
      console.log(data)

      try {
        let response = await fetch('http://localhost:8000/verify_token', {
          method: 'POST',
          body: JSON.stringify(data),
          headers: {
            'Content-Type': 'application/json',
          },
        });

        response = await response.json();
        console.log("/verify_token:response:");
        console.log(response);

        setIsUser(response.verified);
      } catch (error) {
        console.error(error);
      }
    }

    handleVerification();
  }, []);

  return (
    <AppBar position="sticky">
      <Toolbar>
        <HeaderTypography>Olympian Tutors</HeaderTypography>
        <Link underline="none" href="/">
          <Button variant="outlined">Homepage</Button>
        </Link>
        <Link underline="none" href="/courses">
          <Button variant="outlined">Find a Course</Button>
        </Link>
        <Link underline="none" href="/tutors">
          <Button variant="outlined">Find a Tutor</Button>
        </Link>
        <Link underline="none" href="/about">
          <Button variant="outlined">About Us</Button>
        </Link>
        {!isUser && (
          <div>
            <Link underline="none" href="/registration">
              <Button variant="contained">Sign Up</Button>
            </Link>
            <Link underline="none" href="/login">
              <Button variant="contained">Log In</Button>
            </Link>
          </div>
        )}
        {isUser && (
          <AccountController />
        )}
      </Toolbar>
    </AppBar>
  );
}

HeaderMenu.propTypes = {
  token: PropTypes.string.isRequired,
};

export default HeaderMenu;