import math
from ophyd import (Device, EpicsMotor, Signal, Component as Cpt,
                   PseudoSingle, PseudoPositioner,
                   movr)

from ophyd.pseudopos import (real_position_argument,
                             pseudo_position_argument)

from hxntools.device import NamedDevice


# NOTE: NamedDevice will name components exactly as the 'name' argument
#       specifies. Normally, it would be named based on the parent
class HxnMLLSample(NamedDevice):
    ssx = Cpt(EpicsMotor, 'XF:03IDC-ES{Ppmac:1-ssx}Mtr', doc='fine_x')
    ssy = Cpt(EpicsMotor, 'XF:03IDC-ES{Ppmac:1-ssy}Mtr', doc='fine_y')
    ssz = Cpt(EpicsMotor, 'XF:03IDC-ES{Ppmac:1-ssz}Mtr', doc='fine_z')
    sth = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:1-Ax:0}Mtr', doc='theta')

    sx = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:4-Ax:5}Mtr', doc='coarse x')
    sy = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:3-Ax:0}Mtr', doc='coarse y')
    sx1 = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:3-Ax:1}Mtr', doc='coarse x1')
    sz = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:3-Ax:2}Mtr', doc='coarse z')
    sz1 = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:3-Ax:3}Mtr', doc='coarse z1')


smll = HxnMLLSample('', name='smll')
ssx = smll.ssx
ssy = smll.ssy
ssz = smll.ssz
sth = smll.sth

sx = smll.sx
sy = smll.sy
sx1 = smll.sx1
sz = smll.sz
sz1 = smll.sz1


class HxnAnc350_3(Device):
    '''3 axis ANC350'''
    ax0 = Cpt(EpicsMotor, '-Ax:0}Mtr')
    ax1 = Cpt(EpicsMotor, '-Ax:1}Mtr')
    ax2 = Cpt(EpicsMotor, '-Ax:2}Mtr')


class HxnAnc350_4(Device):
    '''4 axis ANC350'''
    ax0 = Cpt(EpicsMotor, '-Ax:0}Mtr')
    ax1 = Cpt(EpicsMotor, '-Ax:1}Mtr')
    ax2 = Cpt(EpicsMotor, '-Ax:2}Mtr')
    ax3 = Cpt(EpicsMotor, '-Ax:3}Mtr')


class HxnAnc350_6(Device):
    '''6 axis ANC350'''
    ax0 = Cpt(EpicsMotor, '-Ax:0}Mtr')
    ax1 = Cpt(EpicsMotor, '-Ax:1}Mtr')
    ax2 = Cpt(EpicsMotor, '-Ax:2}Mtr')
    ax3 = Cpt(EpicsMotor, '-Ax:3}Mtr')
    ax4 = Cpt(EpicsMotor, '-Ax:4}Mtr')
    ax5 = Cpt(EpicsMotor, '-Ax:5}Mtr')


# Note that different controllers have different axis counts:
anc350_1 = HxnAnc350_6('XF:03IDC-ES{ANC350:1', name='anc350_1')
anc350_2 = HxnAnc350_6('XF:03IDC-ES{ANC350:2', name='anc350_2')
anc350_3 = HxnAnc350_4('XF:03IDC-ES{ANC350:3', name='anc350_3')
anc350_4 = HxnAnc350_6('XF:03IDC-ES{ANC350:4', name='anc350_4')
anc350_5 = HxnAnc350_6('XF:03IDC-ES{ANC350:5', name='anc350_5')
anc350_6 = HxnAnc350_6('XF:03IDC-ES{ANC350:6', name='anc350_6')
anc350_7 = HxnAnc350_3('XF:03IDC-ES{ANC350:7', name='anc350_7')
anc350_8 = HxnAnc350_3('XF:03IDC-ES{ANC350:8', name='anc350_8')


class HxnVerticalMLL(NamedDevice):
    vx = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:2-Ax:0}Mtr', doc='coarse x')
    vy = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:2-Ax:1}Mtr', doc='coarse y')
    vz = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:2-Ax:2}Mtr', doc='coarse z')
    vchi = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:2-Ax:4}Mtr', doc='chi')
    vth = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:2-Ax:3}Mtr', doc='theta')


vmll = HxnVerticalMLL('', name='vmll')


class HxnHorizontalMLL(NamedDevice):
    hx = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:2-Ax:5}Mtr', doc='x')
    hy = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:4-Ax:0}Mtr', doc='y')
    hz = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:4-Ax:1}Mtr', doc='z')
    hth = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:1-Ax:2}Mtr', doc='theta')


hmll = HxnHorizontalMLL('', name='hmll')


class HxnMLL_OSA(NamedDevice):
    osax = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:4-Ax:2}Mtr')
    osay = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:4-Ax:3}Mtr')
    osaz = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:4-Ax:4}Mtr')


mllosa = HxnMLL_OSA('', name='mllosa')


class HxnMLLBeamStop(NamedDevice):
    bsx = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:5-Ax:0}Mtr')
    bsy = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:5-Ax:1}Mtr')


mllbs = HxnMLLBeamStop('', name='mllbs')


class PseudoAngleCorrection(PseudoPositioner, NamedDevice):
    '''Pseudo positioner definition for MLL coarse and fine sample positioners
    with angular correction
    '''

    def __init__(self, prefix, **kwargs):
        super().__init__(prefix, **kwargs)

        # if theta changes, update the pseudo position
        self.theta.subscribe(self.parameter_updated)

    def parameter_updated(self, value=None, **kwargs):
        self._update_position()

    @property
    def radian_theta(self):
        return math.radians(self.theta.get())

    @pseudo_position_argument
    def forward(self, position):
        theta = self.radian_theta
        c = math.cos(theta)
        s = math.sin(theta)

        x = c * position.px + s * position.pz
        z = -s * position.px + c * position.pz
        return self.RealPosition(x=x, z=z)

    @real_position_argument
    def inverse(self, position):
        theta = self.radian_theta
        c = math.cos(theta)
        s = math.sin(theta)
        x = c * position.x - s * position.z
        z = s * position.x + c * position.z
        return self.PseudoPosition(px=x, pz=z)


class PseudoMLLFineSample(PseudoAngleCorrection):
    # pseudo axes
    px = Cpt(PseudoSingle, name='pssx')
    pz = Cpt(PseudoSingle, name='pssz')

    # real axes
    x = Cpt(EpicsMotor, 'XF:03IDC-ES{Ppmac:1-ssx}Mtr', name='ssx')
    z = Cpt(EpicsMotor, 'XF:03IDC-ES{Ppmac:1-ssz}Mtr', name='ssz')

    # configuration settings
    theta = Cpt(Signal, value=15.0, name='pmllf_theta')


class PseudoMLLCoarseSample(PseudoAngleCorrection):
    # pseudo axes
    px = Cpt(PseudoSingle, name='psx')
    pz = Cpt(PseudoSingle, name='psz')

    # real axes
    x = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:4-Ax:5}Mtr', name='sx')
    z = Cpt(EpicsMotor, 'XF:03IDC-ES{ANC350:3-Ax:2}Mtr', name='sz')

    # configuration settings
    theta = Cpt(Signal, value=15.0, name='pmllc_theta')


pmllf = PseudoMLLFineSample('', name='pmllf')
pssx = pmllf.x
pssz = pmllf.z
# To tweak the angle, set pmllf.theta.put(15.1) for example


pmllc = PseudoMLLCoarseSample('', name='pmllc')
psx = pmllc.x
psz = pmllc.z


def movr_hth(angle):
    radian = angle * math.pi / 180.0
    correction = -1. * math.tan(radian) * 34376.6
    movr(hmll.th, angle)
    movr(hmll.coarse_x, correction)