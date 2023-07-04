import backgroundImage from '../Images/HomepageBG.png';

export const background = {
  backgroundImage: `url(${backgroundImage})`,
  backgroundSize: 'cover',
  backgroundRepeat: 'repeat',
  backgroundPosition: 'center',
  minHeight: '100vh',
  opacity: 0.4,
  filter: 'blur(0.5px)',
};

export default function Homepage() {
  return (
    <div style={background}/>
  );
}