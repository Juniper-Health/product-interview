const BASE_SERVER_URL = 'http://localhost:8000';

const getPatients = async () => {
    const response = await fetch(`${BASE_SERVER_URL}/patients`);
    const data = await response.json();
    return data;
}

export { getPatients }