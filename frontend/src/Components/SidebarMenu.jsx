import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';

import { Link } from "react-router-dom"
import { useState } from "react"

const listStyle = {
  display: "flex",
  flexDirection: "row",
  padding: 0,
}

export default function SidebarMenu() {
  return (
    <List style={listStyle}>
      <ListItem><Link to="/">Homepage</Link></ListItem>
      <ListItem><Link to="/courses">Find a Course</Link></ListItem>
      <ListItem><Link to="/tutors">Find a Tutor</Link></ListItem>
      <ListItem><Link to="/registration">Register</Link></ListItem>
      <ListItem><Link to="/login">Login</Link></ListItem>
      <ListItem><Link to="/about">About</Link></ListItem>
    </List>
  );
}