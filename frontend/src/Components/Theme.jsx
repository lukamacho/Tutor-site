import { createTheme } from '@mui/material';
import '../Fonts/custom-font.css';

export const customColors = {
  darkPurple: '#420e60',
  greyPurple: '#d9d5de',
  lavenderPurple: '#8e87ff',
  whiteSmoke: '#f5f5f5',
  peachPuff: '#ffeaa7',

  lavender: '#e6e6fa',
  black: '#000000',
  ivory: '#fffff0',
  gainsboro: '#dcdcdc',
};

export const theme = createTheme({
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: '4px',
          textTransform: 'none',
          color: customColors.darkPurple,
          margin: 5,
          '&:hover': {
            boxShadow: '0px 0px',
            borderRadius: '4px',
            color: customColors.greyPurple,
            backgroundColor: customColors.lavenderPurple,
          },
        },
        contained: {
          backgroundColor: customColors.whiteSmoke,
          boxShadow: '0px 0px',
        },
        outlined: {
          borderColor: customColors.darkPurple,
        },
      },
    },
  },
  palette: {
    primary: {
      main: customColors.greyPurple,
    },
    secondary: {
      main: customColors.lavender,
    },
    customColors: {
      darkPurple: customColors.darkPurple,
      greyPurple: customColors.greyPurple,
      lavenderPurple: customColors.lavenderPurple,
      whiteSmoke: customColors.whiteSmoke,
      peachPuff: customColors.peachPuff,
    }
  },
  typography: {
    fontFamily: 'Raleway',
    fontWeightLight: 300,
    fontWeightMedium: 500,
    fontWeightBold: 700,
  },
});
