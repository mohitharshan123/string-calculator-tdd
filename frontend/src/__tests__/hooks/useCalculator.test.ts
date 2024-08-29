import { renderHook, act } from '@testing-library/react-hooks';

import calculatorApi from '../../apis/calculator';
import useCalculator from '../../hooks/useCalculator';
import { AxiosError, AxiosResponse } from 'axios';
import { AxiosHeaders } from 'axios';

jest.mock('../../apis/calculator');

const mockedCalculatorApi = calculatorApi as jest.Mocked<typeof calculatorApi>;

const mockHeaders: AxiosHeaders = {
    get: () => 'application/json',
    set: () => { },
    has: () => true,
    delete: () => { },
} as any;

const createMockAxiosResponse = <T>(data: T): AxiosResponse<T> => ({
    data,
    status: 200,
    statusText: 'OK',
    headers: {},
    config: { headers: mockHeaders }
});


const createMockAxiosError = (data: any, status = 400): AxiosError => ({
    response: {
        data,
        status,
        statusText: 'Bad Request',
        headers: {},
        config: {}
    },
    request: {},
    message: data,
    name: 'AxiosError'
} as any);


describe('useCalculator Hook', () => {
    beforeEach(() => {
        jest.clearAllMocks();
    })

    it('should handle successful API response', async () => {
        const mockResponse = createMockAxiosResponse({ result: 6 });

        mockedCalculatorApi.calculate.mockResolvedValue(mockResponse);

        const { result, waitForNextUpdate } = renderHook(() => useCalculator());

        act(() => {
            result.current.setNumbers('1,2,3');
            result.current.calculate();
        });

        await waitForNextUpdate();

        expect(result.current.state.result).toBe(6);
        expect(result.current.state.error).toBeNull();
        expect(result.current.state.isLoading).toBe(false);
    });

    it('should handle API error response', async () => {
        const mockResponse = createMockAxiosError({ numbers: 'This field is required' });

        mockedCalculatorApi.calculate.mockRejectedValue(mockResponse);

        const { result, waitForNextUpdate } = renderHook(() => useCalculator());

        act(() => {
            result.current.setNumbers('');
            result.current.calculate();
        });

        await waitForNextUpdate();

        expect(result.current.state.result).toBeNull();
        expect(result.current.state.error).toBe('This field is required');
        expect(result.current.state.isLoading).toBe(false);
    });

    it('should handle network errors', async () => {
        const mockResponse = createMockAxiosError(new Error('Network Error'));

        mockedCalculatorApi.calculate.mockRejectedValue(mockResponse);

        const { result, waitForNextUpdate } = renderHook(() => useCalculator());

        act(() => {
            result.current.setNumbers('1,2,3');
            result.current.calculate();
        });

        await waitForNextUpdate();

        expect(result.current.state.result).toBeNull();
        expect(result.current.state.error).toBe('An error occurred');
        expect(result.current.state.isLoading).toBe(false);
    });
});
