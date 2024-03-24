import Confetti from 'react-confetti'
import useWindowSize from 'react-use/lib/useWindowSize'
import {PageLayout} from "@/components/layout/PageLayout.tsx";
import {MapContainer} from "react-leaflet/MapContainer";
import {TileLayer} from "react-leaflet/TileLayer";
import {Marker} from "react-leaflet";
import {Step, StepItem, Stepper } from "@/components/ui/stepper.tsx";
import {Card, CardContent, CardHeader, CardTitle} from "@/components/ui/card.tsx";
import {Button} from "@/components/ui/button.tsx";
import {Book} from "lucide-react";
import {IconFileDownload} from "@tabler/icons-react";
import {Document, Page, pdfjs} from "react-pdf";

pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

export const BolSuccess = () => {
    const { width, height } = useWindowSize()

    return (
        <>
            <Confetti
                width={width}
                height={height}
                recycle={true}
                colors={['#000000', '#1FE7B6']}
                tweenDuration={5000}
            />
            <PageLayout title={"Your eBL is on chain !"} description={"Bravo !"}>
                <div className={"flex flex-col gap-5"}>
                    <StepperDemo/>
                    <MapContainer className={"w-[1650px] h-[300px] z-0"} center={[25, 0]} zoom={1} scrollWheelZoom={false}>
                        <TileLayer
                            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                        />
                        {/* Coord du port de singapore */}
                        <Marker position={[1.290270, 103.851959]}/>
                        {/* Coord du port de hambourg */}
                        <Marker position={[53.5459, 9.9916]}/>
                    </MapContainer>
                    <Card>
                        <CardHeader>
                            <CardTitle>Summary</CardTitle>
                        </CardHeader>
                        <CardContent className={"flex flex-col gap-4"}>
                            <div className={"flex gap-1.5"}>
                                <Button className={"gap-1.5"}>
                                    <IconFileDownload />
                                    Download eBL as PDF
                                </Button>

                                <Button className={"gap-1.5"}>
                                    <Book/>
                                    <a href="https://ghostnet.tzkt.io/KT1MvGPyXNvNNwEAc286Xtw9Xgv5B5vBFHg3/operations/" target="_blank">
                                        On chain proof (Ghostnet)
                                    </a>
                                </Button>
                            </div>
                        </CardContent>
                    </Card>
                </div>
                    <Document file={"http://localhost:5173/bol.pdf"} >
                        <Page pageNumber={1} width={1700}/>
                    </Document>
            </PageLayout>
        </>
    );
}

const steps = [
    {label: "eBL created"},
    {label: "eBL validated by shipper"},
    {label: "eBL validated by consignee"},
    {label: "shipped"},
    {label: "cargo delivered"},
] satisfies StepItem[]
export default function StepperDemo() {
    return (
        <div className="flex w-full flex-row gap-4">
            <Stepper orientation="horizontal" initialStep={1} steps={steps}>
                {steps.map(({ label }) => {
                    return (
                        <Step key={label} label={label}>
                        </Step>
                    )
                })}
            </Stepper>
        </div>
    )
}
