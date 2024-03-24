import {BillOfLading} from "@/types/BillOfLading.ts";
import {getCsrfToken} from "@/services/loginService.tsx";

export const createBol = async (bol: BillOfLading) => {

    const csrfToken = await getCsrfToken();

    const rawResponse = await fetch('http://localhost:8000/dataManagement/manageContract/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                "X-CSRFToken": csrfToken,
            },
            credentials: "include",
            body: JSON.stringify(bol)
        });
        const content = await rawResponse.json();

        console.log(content);
};


export const getBols = async () => {

    const rawResponse = await fetch('http://localhost:8000/dataManagement/manageContract', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
    });
    const content = await rawResponse.json();

    return content.data as BillOfLading[];
};