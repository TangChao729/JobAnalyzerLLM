import React, { useRef } from 'react';
import JobModal from './JobModal';

const JobCard = ({ job }) => {
    const modalRef = useRef(null);

    const handleCardClick = () => {
        if (modalRef.current) {
            modalRef.current.open();
        }
    };

    const closeModal = () => {
        if (modalRef.current) {
            modalRef.current.close();
        }
    };

    return (
        <div className="jobcard" onClick={handleCardClick}>
            <h2>{job.title}</h2>
            <p>{job.company}</p>
            <p>Similarity: {(job._score * 100).toFixed(2)}%</p>
            <JobModal ref={modalRef} job={job} onClose={closeModal} />
        </div>
    );
};

export default JobCard;