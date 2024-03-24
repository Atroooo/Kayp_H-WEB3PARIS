	
![Color_logo_with_background](https://github.com/Atroooo/BPELO/assets/117669219/41792310-cb7b-402a-9e54-0781a5e53cc5)

# Getting Started

Follow these steps to clone the repository and start the development server:

- `git clone https://github.com/Atroooo/BPELO.git`
- `cd frontend`
- `npm install`
- `npm run dev`

In an other terminal

-  Go at the root of the repository
- `pip install -r backend/requirements.txt` (python version needed <= 3.10.12)
- `cd backend`
- `python manage.py runserver`

You should now be able to access the application at http://localhost:5173.

# Front-end

This using the following stack:

- Language - [TypeScript](https://www.typescriptlang.org)
- Styling - [Tailwind CSS](https://tailwindcss.com)
- Components - [Shadcn-ui](https://ui.shadcn.com)
- Schema Validations - [Zod](https://zod.dev)
- State Management - [Zustand](https://zustand-demo.pmnd.rs)
- Forms - [React Hook Form](https://ui.shadcn.com/docs/components/form)
- Linting - [ESLint](https://eslint.org)
- Formatting - [Prettier](https://prettier.io)

## Pages

| Pages                                                                       | Specifications              | Preview
|:----------------------------------------------------------------------------|:----------------------------|---------------------------
| [Login](https://localhost:5173/log-in)                                      | Login page                  | ![image](https://github.com/Atroooo/BPELO/assets/76119301/cbf9f17e-e0a2-463b-b8cd-c1328db440a8)     |
| [Dashboard](https://localhost:5173/)              | Dashboard                   |		            |													  |
| [Create eBL](https://localhost:5173/bol/create)    | Create a new eBL            |			    | ![createEBL](https://github.com/Atroooo/BPELO/assets/76119301/f7840526-9b9c-47ac-8d55-079fccfb1cc1) |
| [List eBL](https://localhost:5173/bol/list) | List and manage all the eBL |				    | ![image](https://github.com/Atroooo/BPELO/assets/76119301/0fdccba2-b96f-4c16-93d4-927bf1d33589)
| 


# Blockchain Implementation
To ensure flawless security, all documents are hashed (encrypted in an irreversible manner), and the hashes are sent to the blockchain. Each bill of lading has a unique ID and a distinct smart contract.

Upon deployment, the main contract initiates a map linking an ID to the corresponding contract address.
When calling the main smart contract, we check if we already know the ID of the bill of lading.

- If it is not recognized, then it is a new document, and the main smart contract called `Deployer` creates a new smart contract that will store the document's hash.
- If it is recognized, then it is a modification of an existing bill of lading. We find the document's smart contract to replace the old hash with the new one.

Each bill of lading has a smart contract that stores its hashed information in the blockchain. They are stored in two ways.
First, the entire document is hashed and store with this setter:
```
@sp.entrypoint
def storeHash(self, whole_hash):
	self.data.stored_whole_hash = whole_hash
```
Then, the document is stored part by part with each part of the document hashed then store in a map. This method allows independent verification of each part of the document:
```
@sp.entrypoint
def storePartHashes(self, part_hashes):
	for item in part_hashes.items():
		self.data.stored_part_hashes[item.key] = item.value
```

### Link of the smart contract
`
https://ghostnet.tzkt.io/KT1QJ3W5d6TidAzFanLJEn4z9WKUPVcTZj1H/storage/
`

# Backend
To deploy the smart contract we need to get every informations needed to create the bill of Lading. 
In order to do that, we use the DCSA API (https://app.swaggerhub.com/apis/dcsaorg/DCSA_EBL/3.0.0-Beta-1) to standardize the documents.
