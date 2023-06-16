import Typography from '@mui/material/Typography';
import { Link } from "react-router-dom"
import Grid from '@mui/material/Grid';

export default function Course(props) {
  return (
    <Grid
      sx={{
        width: "100%",
        borderRadius: "10px",
        backgroundColor: "#92F0E2",
        display: 'flex',
        alignItems: 'center',
        margin: "1px",
        '&:hover': {
          backgroundColor: "#AFFAEF",
          opacity: [0.9, 0.8, 0.7],
        },
      }}
      container
      spacing={2}>
      <Grid item>
        <Typography variant="overline" display="block" gutterBottom>
          {props.subject}
        </Typography>
      </Grid>
      <Grid item>
        <Typography variant="overline" display="block" gutterBottom>
          <Link to={"/tutor/" + props.tutor_mail}>{props.tutor_mail}</Link>
        </Typography>
      </Grid>
      <Grid item>
        <Typography variant="overline" display="block" gutterBottom>
          {props.price}
        </Typography>
      </Grid>
    </Grid>
  )
}