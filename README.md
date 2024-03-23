# Implémentation blockchain
Pour assurer une sécurité sans faille, tous les documents sont hashés (cryptés de manière irréversible), et les hashs sont envoyés sur la blockchain. Chaque bill of lading possède un ID et un smart contract distincts.

Lors de son déploiement, le contrat principal initie une map liant un ID à l'adresse du contrat correspondant.
![carbon(1)](https://github.com/Atroooo/BPELO/assets/117669219/e41105d6-1864-4e96-80c9-d3d508fdbc66)

Lors de l'appel au smart contract principal, nous vérifions si nous connaissons déjà l'ID du bill of lading.
![carbon(4)](https://github.com/Atroooo/BPELO/assets/117669219/9de987ef-d715-4df6-9f6f-8870a2aa0953)

-Si il n'est pas reconnu, alors c'est un nouveau document et le smart contract principal appelé 'Deployer' créé un nouveau smart contract qui va stocker le hash du document.
![carbon(3)](https://github.com/Atroooo/BPELO/assets/117669219/4ab10720-ef74-4efa-a2a0-b0ced7f79bfd)

-Si il est reconnu, alors c'est une modification d'un bill of lading déjà existant. On retrouve le smart contract du document pour modifier l'ancien hash par le nouveau.
![carbon(5)](https://github.com/Atroooo/BPELO/assets/117669219/edc89b75-f246-4630-ab00-af4b7aef6f38)

Chaque bill of lading dispose d'un smart contract stockant dans la blockchain ses informations hashées.
![carbon(7)](https://github.com/Atroooo/BPELO/assets/117669219/32c96232-e627-491f-a33b-47fc44354fe1)
