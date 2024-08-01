import React, { useState, useEffect } from "react";
import chefResume from "../assets/dummy_resume/dummy_Chef.txt";
import divingCoachResume from "../assets/dummy_resume/dummy_DivingCoach.txt";
import estimatorResume from "../assets/dummy_resume/dummy_Estimator.txt";
import softwareEngineerResume from "../assets/dummy_resume/dummy_SE.txt";
import tutorResume from "../assets/dummy_resume/dummy_Tutor.txt";

const UserProfileInput = ({ setUserProfile, handleSubmitProfile }) => {
  const [manualInput, setManualInput] = useState("");
  const [selectedResume, setSelectedResume] = useState("");

  useEffect(() => {
    if (selectedResume) {
      fetch(selectedResume)
        .then((response) => response.text())
        .then((text) => setManualInput(text));
    }
  }, [selectedResume]);

  const handleManualSubmit = (e) => {
    e.preventDefault();
    setUserProfile(manualInput);
    handleSubmitProfile(manualInput);
  };

  const handleManualClick = () => {
    setManualInput("");
    setSelectedResume("");
  };

  const handleResumeSelect = (e) => {
    setSelectedResume(e.target.value);
  };

  return (
    <div id="quiz">
      <div>
        <button onClick={handleManualClick}>Manual</button>
        <select onChange={handleResumeSelect} value={selectedResume}>
          <option value="" disabled>
            Select a resume
          </option>
          <option value={chefResume}>Sample Chef Resume</option>
          <option value={divingCoachResume}>Sample Diving Coach Resume</option>
          <option value={estimatorResume}>Sample Estimator Resume</option>
          <option value={softwareEngineerResume}>
            Sample Software Engineer Resume
          </option>
          <option value={tutorResume}>Sample Tutor Resume</option>
        </select>
      </div>

      <form onSubmit={handleManualSubmit}>
        <textarea
          value={manualInput}
          onChange={(e) => setManualInput(e.target.value)}
          placeholder="Type your experience, qualifications, skills, and desired job title here..."
          rows="10"
          cols="50"
        />
        <div className="submit-container">
          <button type="submit">Submit</button>
        </div>
      </form>
    </div>
  );
};

export default UserProfileInput;