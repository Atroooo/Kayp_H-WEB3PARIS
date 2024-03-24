import { CardsStats } from "@/components/charts/Charts.tsx";
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table";
import {PageLayout} from "@/components/layout/PageLayout.tsx";
import {Separator} from "@/components/ui/separator.tsx";
import {BillOfLading} from "@/types/BillOfLading.ts";
import {useEffect, useState} from "react";
import {getBols} from "@/services/bolService.ts";

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
    const [data, setData] = useState<BillOfLading[]>([]);

    useEffect(() => {
        getBols().then((bols) => setData(bols as unknown as BillOfLading[]));
    }, [])
    return (
        <TableBody className="">
            {data.map((d) => (
                    <TableRow
                        key={d.shipper.name}
                        className=" hover:bg-slate-900 hover:text-slate-50"
                    >
                        <TableCell>{d.shipper.name}</TableCell>
                        <TableCell>{d.vesselDetails.destinationPort}</TableCell>
                        <TableCell>{d.consignee.name}</TableCell>
                        <TableCell className="text-right">{d.vesselDetails.destinationPort}</TableCell>
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
