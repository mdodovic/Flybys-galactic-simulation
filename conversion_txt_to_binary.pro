N=70000      ; total number of particles
Nd=15000      ; disk particles
Nb=5000     ; bulge particles
Nh=50000      ; halo particles
;Ns=             ;"stars"
unit_gal_mass=2.325e9  
unit_gad_mass=1.e10


xx=fltarr(7,N)
openu, 2, "C:/Users/matij/Desktop/Projekat_2017-Flybays/galaxy.txt"
readf, 2, xx
close, 2

massconversion=unit_gal_mass/unit_gad_mass
mpd=xx[0,0]
mpb=xx[0,Nd]
mph=xx[0,Nd+Nb]
;mps=xx[0,Nd+Nb+Nh]

print, mpd, mpb, mph ;, mps

tempd=fltarr(7,Nd)
tempb=fltarr(7,Nb)
temph=fltarr(7,Nh)
;emps=fltarr(7,Ns)
print, 'galactICS mass in halo=', mph*Nh*unit_gal_mass
print, 'galactICS mass in disk=', mpd*Nd*unit_gal_mass
print, 'galactICS mass in bulge=', mpb*Nb*unit_gal_mass
;print, 'galactICS mass in stars=', mps*Ns*unit_gal_mass

tempd=xx[*,0:Nd-1]
tempb=xx[*,Nd:Nd+Nb-1]
temph=xx[*,Nd+Nb:Nd+Nb+Nh-1]
;temps=xx[*,Nd+Nb+Nh:Nd+Nb+Nh+Ns-1]

xx[*,0:Nh-1]=temph
xx[*,Nh:Nh+Nd-1]=tempd
xx[*,Nh+Nd:Nh+Nd+Nb-1]=tempb
;xx[*,Nh+Nd+Nb:Nh+Nd+Nb+Ns-1]=temps


;;;;;;;;;;;;;;;;;;;;;;;;;    create halo + disk + bulge 
;;;;;;;;;;;;;;;;;;;;;;;;;    isolated     

    openw, 4, 'C:/Users/matij/Desktop/Projekat_2017-Flybays/GALAKSIJA',/f77_unformatted


npart=lonarr(6)
npart[1]=Nh
npart[2]=Nd
npart[3]=Nb
;npart[4]=Ns

;xi=10.1541     ; in case you want to offset the galaxy
;yi=36.6580
;zi=18.2089
pos=fltarr(3,N)
pos[0,*]=xx[1,*];+xi       ; in case you want to offset the galaxy
pos[1,*]=xx[2,*];+yi       ; add xi, yi, zi
pos[2,*]=xx[3,*];+zi

vel=fltarr(3,N)
vel[0,*]=xx[4,*]*100.
vel[1,*]=xx[5,*]*100.
vel[2,*]=xx[6,*]*100.

;     d=sqrt((x0-pos[0,*])^2.+(y0-pos[1,*])^2.+(z0-pos[2,*])^2.)
;     xort=(x0-pos[0,*])/d
;     yort=(y0-pos[1,*])/d
;     zort=(z0-pos[2,*])/d

;     kick=1000.

;     vxkick=kick*xort
;     vykick=kick*yort
;     vzkick=kick*zort

     vxkick=-4.83452
     vykick=-62.0415
     vzkick=-39.0725
     vel[0,*]=vel[0,*];+vxkick   ; if you want to kick the galaxy
     vel[1,*]=vel[1,*];+vykick
     vel[2,*]=vel[2,*];+vzkick

massarr=dblarr(6)

massarr[1]=mph*massconversion
massarr[2]=mpd*massconversion
massarr[3]=mpb*massconversion
;massarr[4]=mps*massconversion
print, 'gadget mass in halo=', massarr[1]*Nh*unit_gad_mass 
print, 'gadget mass in disk=', massarr[2]*Nd*unit_gad_mass 
print, 'gadget mass in bulge=', massarr[3]*Nb*unit_gad_mass 
;print, 'gadget mass in stars=', massarr[4]*Ns*unit_gad_mass

id=lindgen(N)

    time=0.0D
    redshift=0.0D
    flag_sfr=0L
    flag_feedback=0L
    npartTotal=lonarr(6)
    npartTotal[1]=Nh
    npartTotal[2]=Nd
    npartTotal[3]=Nb
    ;npartTotal[4]=Ns 
    bytesleft=256-6*4 - 6*8 - 8 - 8 - 2*4-6*4
    la=intarr(bytesleft/2)

    writeu,4,npart,massarr,time,redshift,flag_sfr,flag_feedback,npartTotal,la
    writeu,4,pos
    writeu,4,vel
    writeu,4,id

    close, 4


end
