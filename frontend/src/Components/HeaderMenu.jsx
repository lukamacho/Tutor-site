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

  console.log("token")
  console.log(token)

  useEffect(() => {
    const handleVerification = async () => {
      let tokenStr = token === null ? "" : token
      let emailToken = JSON.parse(sessionStorage.getItem('token'))
      let emailStr = emailToken === null ? "" : emailToken

      const data = {
        "token": tokenStr,
        "email": emailStr,
      }

      console.log(data);

      try {
        let response = await fetch('http://localhost:8000/verify_token', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        });

        response = await response.json();
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
  token: PropTypes.func.isRequired,
};

export default HeaderMenu;