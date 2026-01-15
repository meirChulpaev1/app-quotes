import { useEffect, useState } from "react";

function RandomJoke() {
    const [joke, setJoke] = useState(Object);
    const [click, setClick] = useState(false);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('https://official-joke-api.appspot.com/random_joke')
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data:object = await response.json()
                setJoke(data)
            } catch (err: any) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        }
        fetchData()

    }, [click]);

    if (loading) {
        return <div>Loading data...</div>;
    }
    if (error) {
        return <div>Error: {error}</div>;
    }
    return (
        <>
            <div className="joke">
              ____
                <h2>Because it's empty here, I added a random joke.</h2>
                <h3>- {JSON.stringify(joke["setup"])} </h3>
                <h3>- {JSON.stringify(joke["punchline"])}</h3>
                <p>h-hhh-h-h</p>
            <button className="buttonfilter" onClick={() => {setClick(!click) }}>get Another joke?</button>
            </div>
        </>
    )
}

export default RandomJoke