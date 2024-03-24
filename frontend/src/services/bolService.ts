import {BillOfLading} from "@/types/BillOfLading.ts";

export const createBol = async (bol: BillOfLading) => {

        const rawResponse = await fetch('http://localhost:8000/manageContract', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(bol)
        });
        const content = await rawResponse.json();

        console.log(content);
};


export const getBols = async () => {

    const rawResponse = await fetch('http://localhost:8000/manageContract', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
    });
    const content = await rawResponse.json();

    return content.data as BillOfLading[];
};