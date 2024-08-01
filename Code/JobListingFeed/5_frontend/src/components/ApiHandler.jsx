export default ApiHandler = ({URL, task, payload }) => {

    fetch(`${URL}/${task}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
    })
    .then(response => response.json())
    .then(data => {
        return data;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
};

