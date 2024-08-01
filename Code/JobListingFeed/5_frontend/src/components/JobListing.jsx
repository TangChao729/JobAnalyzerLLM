import React from 'react';
import JobCard from './JobCard';

const JobListing = ({ jobs, onAnalyze }) => {
    return (
        <div id="quiz" className="job-listing">
            {jobs.map((job, index) => (
                <JobCard key={index} job={job} />
            ))}
            <div className="submit-container">
                <button type="submit" onClick={onAnalyze}>Analyze</button>
            </div>
        </div>
    );
};

export default JobListing;