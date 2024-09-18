import logo from './logo.svg';
import './App.css';
import AppRouter  from './AppRouter'
import icon from './assets/favicon.ico';
import React, { useEffect} from 'react';

const App = () => {
  useEffect(() => {
    const favicon = document.getElementById('favicon');
    if (favicon) {
      favicon.setAttribute('href', icon);
    }
  }, []);

  return (
    <AppRouter></AppRouter>
);
}
export default App;
