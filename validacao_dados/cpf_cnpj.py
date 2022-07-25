from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return DocCpf(doc_str)
        elif len(doc_str) == 14:
            return DocCnpj(doc_str)
        elif len(doc_str) == 20:
            return DocQualquer(doc_str)
        else:
            raise ValueError("Quantidade de dígitos incorreta!")


class DocQualquer:
    pass


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        mascara = CNPJ()
        return mascara.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)


class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if tipo_documento == "cpf":
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF Invalido!")
        elif self.tipo_documento == "cnpj":
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ Invalido!")
        else:
            raise ValueError("Documento Invalido")

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos inválida")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.format_cpf()
        elif self.tipo_documento == "cnpj":
            return self.format_cnpj()

    def cnpj_e_valido(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("O Cnpj não é valido")
