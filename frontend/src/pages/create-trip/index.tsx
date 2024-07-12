/* eslint-disable @typescript-eslint/no-unused-vars */
import { FormEvent, useState } from "react"
import { useNavigate } from "react-router-dom"
import { InviteGuestsModal } from "./invite-guests-modal"
import { ConfirmTripModal } from "./confirm-trip-modal"
import { DestinationDateStep } from "./steps/destination-date-step"
import { InviteGuestsStep } from "./steps/invite-guests-step"
import { DateRange } from "react-day-picker"
import { api } from "../../lib/axios"

export function CreateTripPage() {
    const [isGuestsInputOpen, setIsGuestsInputOpen] = useState(false)
    const [isGuestsModalOpen, setIsGuestsModalOpen] = useState(false)
    const [isConfirmTripModalOpen, setIsConfirmTripModalOpen] = useState(false)
    const [emailsToInvite, setEmailsToInvite] = useState<string[]>([])

    const [destination, setDestination] = useState('')
    const [ownerName, setOwnerName] = useState('')
    const [ownerEmail, setOwnerEmail] = useState('')
    const [eventDate, setEventDate] = useState<DateRange | undefined>()



    const navigate = useNavigate()

    function openGuestsInput() {
        setIsGuestsInputOpen(true)
    }

    function openGuestsModal() {
        setIsGuestsModalOpen(true)
    }
    function openConfirmTripModal() {
        setIsConfirmTripModalOpen(true)
    }

    function closeGuestsModal() {
        setIsGuestsModalOpen(false)
    }

    function closeGuestsInput() {
        setIsGuestsInputOpen(false)
    }

    function closeConfirmTripModal() {
        setIsConfirmTripModalOpen(false)
    }

    function AddEmailToInvite(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()

        const data = new FormData(event.currentTarget)
        const email = data.get('email')?.toString()

        if (!email) {
            return
        }

        if (emailsToInvite.includes(email)) {
            return
        }

        setEmailsToInvite([...emailsToInvite, email])

        event.currentTarget.reset()
    }

    function removeEmailFromInvites(emailToRemove: string) {
        const newEmailList = emailsToInvite.filter(email => email !== emailToRemove)

        setEmailsToInvite(newEmailList)
    }

    async function createTrip(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()

        if (!destination) {
            return
        }

        if (!eventDate?.from || !eventDate?.to) {
            return
        }

        if (!ownerName || !ownerEmail) {
            return
        }

        const response = await api.post('/trips/', {
            destination: destination,
            starts_at: eventDate.from,
            ends_at: eventDate.to,
            owner_name: ownerName,
            owner_email: ownerEmail,
            emails_to_invite: emailsToInvite
        })

        const trip = response.data

        navigate(`/trips/${trip.id}`)
    }

    return (
        <div className="h-screen flex items-center justify-center bg-pattern bg-no-repeat bg-center">
            <div className="max-w-3xl w-full px-6 text-center space-y-10">
                <div className="flex flex-col items-center gap-3">
                    <img src="/logo.png" alt="plann.er" />
                    <p className="text-zinc-300 text-lg">Convide seus amigos e planeje a sua próxima viagem!</p>
                </div>

                <div className="space-y-4">
                    <DestinationDateStep
                        closeGuestsInput={closeGuestsInput}
                        isGuestsInputOpen={isGuestsInputOpen}
                        openGuestsInput={openGuestsInput}
                        setDestination={setDestination}
                        eventDate={eventDate}
                        setEventDate={setEventDate}
                    />

                    {isGuestsInputOpen && (
                        <InviteGuestsStep
                            emailsToInvite={emailsToInvite}
                            openConfirmTripModal={openConfirmTripModal}
                            openGuestsModal={openGuestsModal}
                        />
                    )}
                </div>

                <p className="text-sm text-zinc-500">
                    Ao planejar sua viagem pela plann.er você automaticamente concorda <br />
                    com nossos <a href="#" className="text-zinc-300 underline">termos de uso</a> e <a href="#" className="text-zinc-300 underline">políticas de privacidade</a>.
                </p>

                {isGuestsModalOpen && (
                    <InviteGuestsModal
                        AddEmailToInvite={AddEmailToInvite}
                        emailsToInvite={emailsToInvite}
                        removeEmailFromInvites={removeEmailFromInvites}
                        closeGuestsModal={closeGuestsModal}
                    // setEmailsToInvite={setEmailsToInvite}
                    />
                )}

                {isConfirmTripModalOpen && (
                    <ConfirmTripModal
                        closeConfirmTripModal={closeConfirmTripModal}
                        createTrip={createTrip}
                        // eventDate={eventDate}
                        destination={destination}
                        setOwnerEmail={setOwnerEmail}
                        setOwnerName={setOwnerName}
                    />
                )}
            </div>
        </div>
    )
}