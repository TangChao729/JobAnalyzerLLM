import React from 'react';

const Navigation = ({ resetState }) => {
    return (
        <nav id="quiz">
            <button onClick={resetState}>New Job</button>
        </nav>
    );
};

export default Navigation;