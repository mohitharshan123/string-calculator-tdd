import { FormEvent } from 'react';
import './App.css';

import useCalculator from './hooks/useCalculator';
import Form from './components/Form';
import Spinner from './components/Spinner';


const App = () => {
  const { state, setNumbers, calculate } = useCalculator();
  const { numbers, result, error, isLoading } = state;

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    calculate();
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen min-w-screen">
      <h1 className="text-4xl font-bold mb-6 text-blue-600">String Calculator</h1>
      <Form input={numbers} setInput={setNumbers} onSubmit={handleSubmit} {...{ isLoading }} />
      <div className='mt-4'>
        {isLoading ? <Spinner /> : <>
          {result !== null && (
            <p className="text-xl font-semibold text-green-600">Result: {result}</p>
          )}

        </>
        }
      </div>
      {error && !isLoading && (
        <p className="mt-4 text-xl font-semibold text-red-600">{error}</p>
      )}
    </div>
  );
}

export default App;
