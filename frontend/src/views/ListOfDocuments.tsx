import { CardsStats } from "@/components/charts/Charts.tsx";
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table";
import { dataListOfDocuments } from "@/data/DataListOfDocuments.tsx";
import {PageLayout} from "@/components/layout/PageLayout.tsx";
import {Separator} from "@/components/ui/separator.tsx";

function Statistics(): JSX.Element {
    return (
        <div>
            <CardsStats />
        </div>
    );
}

export interface DataTable {
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
        <div>
            <h3 className="text-2xl font-semibold leading-none tracking-tight text-start">History</h3>
            <div className=" max-h-96 overflow-y-auto ">
                <Table className="mt-5 border ">
                    <DataTableHeader/>
                    <DataTableBody/>
                </Table>
            </div>
        </div>
    );
}

export function ListOfDocuments() {
    return (
        <PageLayout title={"Dashboard"} description={"some statistics..."}>
            <div className={"flex flex-col gap-12"}>
                <Statistics />
                <Separator />
                <DataTable />
            </div>
        </PageLayout>
    );
}
