import React from 'react';
import logoImg from '../assets/JAL.png';

const Header = () => {
    return (
        <header>
            <img src={logoImg} alt='JAL logo' />
            <h1>Job Analyser</h1>
        </header>
    );
};

export default Header;

