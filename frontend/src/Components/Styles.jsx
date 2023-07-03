import { styled } from '@mui/system';
import Typography from '@mui/material/Typography';
import { customColors } from './Theme'

export const HeaderTypography = styled(Typography)(({ theme }) => ({
  color: customColors.darkPurple,
  fontWeight: 'normal',
  fontSize: 34,
  flexGrow: 1,
}));

export const StyledTypography = styled(Typography)(({ theme }) => ({
  flexGrow: 1,
  marginLeft: theme.spacing(2),
  fontWeight: 'bold',
  color: '#1f53a1',
  display: 'flex',
  alignItems: 'center',
  flexWrap: 'wrap',
}));

export const CourseStyledTypography = styled(Typography)(({ theme }) => ({
  fontWeight: 'medium',
  color: '#320f70',
  display: 'flex',
  alignItems: 'center',
  flexWrap: 'wrap',
}));

export const TutorStyledTypography = styled(Typography)(({ theme }) => ({
  fontWeight: 'medium',
  color: '#320f70',
  display: 'flex',
  alignItems: 'center',
  flexWrap: 'wrap',
}));

export const HeaderStyledTypography = styled(Typography)(({ theme }) => ({
  fontWeight: 'light',
  fontSize: "48px",
  color: '#663296',
  alignItems: 'center',
  flexWrap: 'wrap',
  padding: 10,
}));