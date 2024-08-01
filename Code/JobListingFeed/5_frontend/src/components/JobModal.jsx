import React, { forwardRef, useImperativeHandle, useRef, useEffect } from 'react';
import ReactDOM from 'react-dom';

const JobModal = forwardRef(({ job, onClose }, ref) => {
    const modalRef = useRef(null);

    useImperativeHandle(ref, () => ({
        open: () => {
            if (modalRef.current) {
                modalRef.current.style.display = 'block';
                modalRef.current.showModal();
            }
        },
        close: () => {
            if (modalRef.current) {
                modalRef.current.style.display = 'none';
                modalRef.current.close();
            }
        }
    }));

    const handleOutsideClick = (e) => {
        if (e.target === modalRef.current) {
            onClose();
        }
    };

    useEffect(() => {
        const modal = modalRef.current;
        if (modal) {
            modal.addEventListener('close', onClose);
            return () => {
                modal.removeEventListener('close', onClose);
            };
        }
    }, [onClose]);

    return ReactDOM.createPortal(
        <dialog className="modal" ref={modalRef} onClick={handleOutsideClick}>
            <div className="modal-content">
                <span className="close" onClick={onClose}>&times;</span>
                <h2>{job.title}</h2>
                <p>{job.description}</p>
                <p>Company ID: {job.company_id}</p>
                <p>Location: {job.location}</p>
                <p>Experience Level: {job.formatted_experience_level}</p>
                <p>Work Type: {job.formatted_work_type}</p>
                <p>Posted on: {new Date(job.listed_time).toLocaleDateString()}</p>
                <p>Job Posting URL: <a href={job.job_posting_url} target="_blank" rel="noopener noreferrer">Apply Here</a></p>
            </div>
        </dialog>,
        document.body
    );
});

export default JobModal;