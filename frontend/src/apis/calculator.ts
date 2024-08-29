import apiClient from ".";

const routes = {
    calculate: "calculator/add/",
};

const calculate = (input: string) =>
    apiClient.post(routes.calculate, { numbers: input });

const calculatorApi = { calculate };

export default calculatorApi;