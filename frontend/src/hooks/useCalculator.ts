import { useState } from 'react';
import calculatorApi from '../apis/calculator';

const useCalculator = () => {
    const [state, setState] = useState<{
        numbers: any;
        result: number | null;
        error: string | null;
        isLoading: boolean;
    }>({
        numbers: '',
        result: null,
        error: null,
        isLoading: false,
    });

    const setNumbers = (numbers: string) => {
        setState((prevState) => ({ ...prevState, numbers }));
    };

    const calculate = async () => {
        setState((prevState) => ({ ...prevState, isLoading: true, result: null, error: null }));

        try {
            const response = await calculatorApi.calculate(state.numbers)
            setState((prevState) => ({
                ...prevState,
                result: response.data.result ?? null,
                error: null,
                isLoading: false,
            }));

        } catch (error) {
            setState((prevState) => ({
                ...prevState,
                result: null,
                error: (error as any).response?.data["numbers"] || 'An error occurred',
                isLoading: false,
            }));
        }
    };

    return {
        state,
        setNumbers,
        calculate,
    };
};

export default useCalculator;
