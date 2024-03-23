import { CardsStats } from "@/components/Charts";
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table";
import { dataListOfDocuments } from "@/services/dataListOfDocuments";

function Statistics(): JSX.Element {
    return (
        <div>
            <h1 className="mb-5 text-4xl">Some statistics.</h1>
            <CardsStats />
        </div>
    );
}

interface DataTable {
    id: string;
    status: string;
    issuer: string;
    date: string;
}

function DataTableHeader(): JSX.Element {
    return (
        <TableHeader>
            <TableRow>
                <TableHead className=" font-bold">ID</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Issuer</TableHead>
                <TableHead className="text-right">Date</TableHead>
            </TableRow>
        </TableHeader>
    );
}

function DataTableBody(): JSX.Element {
    return (
        <TableBody className="">
            {dataListOfDocuments
                .slice()
                .reverse()
                .map((row) => (
                    <TableRow
                        key={row.id}
                        className=" hover:bg-slate-900 hover:text-slate-50"
                    >
                        <TableCell>{row.id}</TableCell>
                        <TableCell>{row.status}</TableCell>
                        <TableCell>{row.issuer}</TableCell>
                        <TableCell className="text-right">{row.date}</TableCell>
                    </TableRow>
                ))}
        </TableBody>
    );
}

function DataTable(): JSX.Element {
    return (
        <div className="mt-20">
            <h3 className=" text-4xl">Bill of landing history</h3>
            <div className=" max-h-96 overflow-y-auto ">
                <Table className="mt-5 border ">
                    <DataTableHeader />
                    <DataTableBody />
                </Table>
            </div>
        </div>
    );
}

export function ListOfDocuments() {
    return (
        <div className=" m-20">
            <Statistics />
            <DataTable />
        </div>
    );
}
