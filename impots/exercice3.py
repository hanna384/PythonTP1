def mesImpots(revenu):
    if (revenu < 9964):
        return '0'
    if (revenu >= 9964 and revenu < 27519):
        return revenu * 0.14
    if (revenu >= 27519 and revenu < 73779):
        return revenu * 0.30
    if (revenu >= 73779 and revenu < 156244):
        return revenu * 0.41
    if (revenu >= 156244):
        return revenu * 0.45
    