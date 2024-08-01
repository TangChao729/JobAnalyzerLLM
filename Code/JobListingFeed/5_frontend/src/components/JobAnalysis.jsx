import React from 'react';

const JobAnalysis = ({ analysis }) => {
    return (
        <div id="quiz">
            <h2>Job Analysis</h2>
            {Object.keys(analysis).map(key => (
                <div key={key}>
                    <h3>{key}</h3>
                    <p>{analysis[key]}</p>
                </div>
            ))}
        </div>
    );
};

export default JobAnalysis;