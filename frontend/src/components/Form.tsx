import React, { ChangeEvent, FormEvent } from 'react';

interface FormProps {
    input: string;
    setInput: (value: string) => void;
    onSubmit: (e: FormEvent<HTMLFormElement>) => void;
    isLoading: boolean;
}

const Form: React.FC<FormProps> = ({ input, setInput, onSubmit, isLoading }) => (
    <form onSubmit={onSubmit} className="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
        <textarea
            placeholder="Enter input"
            value={input}
            onChange={(e: ChangeEvent<HTMLTextAreaElement>) => setInput(e.target.value)}
            className="w-full p-3 border border-gray-300 rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
            type="submit"
            className="w-full justify-center items-center flex bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            disabled={isLoading}
        >
            Calculate
        </button>
    </form>
);

export default Form;
