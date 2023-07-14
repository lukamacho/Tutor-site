import { Container, Box } from "@mui/material"
import Typography from "@mui/material/Typography"
import IconButton from "@mui/material/IconButton"
import { useState } from "react"
import Avatar from "@mui/material/Avatar"
import Menu from "@mui/material/Menu"
import MenuItem from "@mui/material/MenuItem"
import Divider from "@mui/material/Divider"
import ListItemIcon from "@mui/material/ListItemIcon"
import PersonIcon from "@mui/icons-material/Person"
import Logout from "@mui/icons-material/Logout"
import { Link } from "react-router-dom"

export default function AccountController() {
  let email =
    localStorage.getItem("email") === "undefined"
    ? null
    : JSON.parse(localStorage.getItem("email"));
  let profileImage =
    sessionStorage.getItem("profileImage") === "undefined"
    ? null
    : JSON.parse(sessionStorage.getItem("profileImage"));

  console.log(email)
  console.log(profileImage)

  const [anchorEl, setAnchorEl] = useState(null);
  const open = Boolean(anchorEl);

  const handleClick = (e) => {
    setAnchorEl(e.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleClickProfile = () => {
    console.log("handleClickProfile");
    handleClose();
  };

  const handleClickLogOut = () => {
    console.log("handleClickLogOut");

    email = null
    profileImage = null

    sessionStorage.setItem("email", JSON.stringify(''));
    sessionStorage.setItem("token", JSON.stringify(''));
    sessionStorage.setItem("profileImage", JSON.stringify(''));

    handleClose();
  };

  return (
    <div>
      { email !== null && (
        <Container>
          <Box
            sx={{
              alignItems: "center",
              display: "flex",
              textAlign: "center"
            }}
          >
            <IconButton
              aria-controls={open ? "account-control-menu" : undefined}
              aria-expanded={open ? "true" : undefined}
              aria-haspopup="true"
              onClick={handleClick}
              size="small"
            >
              <Avatar
                src={
                  profileImage === null
                  ? require("../Storage/default")
                  : require("../Storage/" + email)
                }
                sx={{
                  height: 32,
                  width: 32
                }}
              >
              </Avatar>
            </IconButton>
          </Box>
          <Menu
            anchorEl={anchorEl}
            id="account-control-menu"
            onClick={handleClose}
            onClose={handleClose}
            open={open}
          >
            <MenuItem onClick={handleClickProfile}>
              <ListItemIcon>
                <PersonIcon fontSize="small" />
              </ListItemIcon>
              <Link to="/student_profile">My Profile</Link>
            </MenuItem>
            <Divider />
            <MenuItem onClick={handleClickLogOut}>
              <ListItemIcon>
                <Logout fontSize="small" />
              </ListItemIcon>
              <Link to="/">Log Out</Link>
            </MenuItem>
          </Menu>
        </Container>
      )}
    </div>
  );
}