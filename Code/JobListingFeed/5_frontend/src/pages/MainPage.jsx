import React, { useState } from 'react';
import Header from '../components/Header';
import Navigation from '../components/Navigation';
import UserProfileInput from '../components/UserProfileInput';
import JobListing from '../components/JobListing';
import JobAnalysis from '../components/JobAnalysis';
import Footer from '../components/Footer';

const MainPage = () => {
    const initialState = {
        userProfile: null,
        jobListings: { hits: [] },
        analysis: null,
    };

    const [state, setState] = useState(initialState);
    // const API_URL = process.env.REACT_APP_API_URL || "http://192.168.31.45:8888";
    const API_URL = "http://144.134.10.154:8888";

    const resetState = () => {
        setState(initialState);
    };

    const handleSubmitProfile = (profile) => {
        const comparePayload = {
            'query': {
                'description': profile,
            }
        };

        fetch(`${API_URL}/search`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(comparePayload),
        })
        .then(response => response.json())
        .then(data => {
            setState(prevState => ({ ...prevState, userProfile: profile, jobListings: data, analysis: null }));
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    };

    const handleAnalyzeJobs = () => {
        const comparePayload = {
            'user_info': state.userProfile,
            'similar_job_description': state.jobListings.hits
        };

        fetch(`${API_URL}/compare`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(comparePayload),
        })
        .then(response => response.json())
        .then(data => {
            try {
                const parsedResponse = JSON.parse(data.response);
                setState(prevState => ({ ...prevState, analysis: parsedResponse }));
            } catch (error) {
                console.error('Error parsing response:', error);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    };

    return (
        <div>
            <Header />
            <Navigation resetState={resetState} />
            <div>
                <UserProfileInput 
                    setUserProfile={(profile) => setState(prevState => ({ ...prevState, userProfile: profile }))}
                    handleSubmitProfile={handleSubmitProfile} 
                />
                {state.userProfile && (
                    <>
                        <JobListing jobs={state.jobListings.hits} onAnalyze={handleAnalyzeJobs} />
                        {state.analysis && (
                            <JobAnalysis analysis={state.analysis} />
                        )}
                    </>
                )}
            </div>
            <Footer />
        </div>
    );
};

export default MainPage;