import { ArrowRight, Calendar, MapPin, Settings2, X } from "lucide-react"
import { Button } from "../../../components/button"
import { useState } from "react"
import { DateRange, DayPicker } from "react-day-picker"
import "react-day-picker/dist/style.css"
import "../../../styles/custom-day-picker.css"
import { format } from "date-fns"

interface DestinationDateStepProps {
    isGuestsInputOpen: boolean
    closeGuestsInput: () => void
    openGuestsInput: () => void
    setDestination: (destination: string) => void
    setEventDate: (dates: DateRange | undefined) => void
    eventDate: DateRange | undefined
}

export function DestinationDateStep({
    closeGuestsInput,
    isGuestsInputOpen,
    openGuestsInput,
    setDestination,
    setEventDate,
    eventDate
}: DestinationDateStepProps) {
    const [isDatePickerOpen, setIsDatePickerOpen] = useState(false)


    function openDatePicker() {
        return setIsDatePickerOpen(true)
    }

    function closeDatePicker() {
        return setIsDatePickerOpen(false)
    }

    const displayedDate = eventDate && eventDate.from && eventDate.to
        ? format(eventDate.from, "d' de 'LLL").concat(' até ').concat(format(eventDate.to, "d' de 'LLL"))
        : null

    return (
        <div className="h-16 bg-zinc-900 px-4 rounded-xl flex items-center shadow-shape gap-3">
            <div className="flex items-center gap-2 flex-1">
                <MapPin className="size-5 text-zinc-400" />
                <input
                    disabled={isGuestsInputOpen}
                    type="text"
                    placeholder="Para onde você vai?"
                    className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
                    onChange={event => setDestination(event.target.value)}
                />
            </div>
            <button
                onClick={openDatePicker}
                disabled={isGuestsInputOpen}
                className="flex items-center gap-2 text-left w-[220px]"
            >
                <Calendar className="size-5 text-zinc-400" />
                <span className="text-lg text-zinc-400 w-40 flex-1">
                    {displayedDate || 'Quando?'}
                </span>
            </button>

            {isDatePickerOpen && (
                <div className="fixed inset-0 bg-black/60 flex items-center justify-center">
                    <div className="rounded-xl py-5 px-6 shadow-shape bg-zinc-900 space-y-5">
                        <div className="space-y-2">
                            <div className="flex items-center justify-between">
                                <h2 className="text-lg font-semibold">Selecione a data</h2>
                                <button type="button" onClick={closeDatePicker}>
                                    <X className="text-zinc-400 hover:bg-lime-400 rounded-full p-1" />
                                </button>
                            </div>
                        </div>
                        <DayPicker mode="range" selected={eventDate} onSelect={setEventDate} />
                    </div>
                </div>
            )}


            <div className="w-px h-6 bg-zinc-800" />

            {!isGuestsInputOpen ? (
                <Button onClick={openGuestsInput} variant="primary">
                    Continuar
                    <ArrowRight className="size-5" />
                </Button>
            ) : (
                <Button onClick={closeGuestsInput} variant="secondary">
                    Alterar local/data
                    <Settings2 className="size-5" />
                </Button>

            )}
        </div>
    )
}