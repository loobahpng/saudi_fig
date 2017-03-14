load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"  
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"  
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"
;************************************************
begin
    x1=asciiread("/work4/L.r02229011/FAO_irrigation/gmia_v5_aai_pct_aei.asc" , -1, "float")
;    varname="area actually irrigated expressed as percentage of area equipped for irrigation"
    x2=asciiread("/work4/L.r02229011/FAO_irrigation/gmia_v5_aei_pct.asc" , -1, "float")
;    varname="area equipped for irrigation expressed as percentage of total area"
    
    varname="Area actually irrigated as percentage of total area"
    Var1=onedtond(x1(6:),(/2160,4320/))
    Var2=onedtond(x2(6:),(/2160,4320/))
  Var=Var1*Var2/100
;  Var=Var1
  Var@long_name="irrigation"
  Var@units=""
lon=fspan(-180,180,4320)
lat=fspan(90,-90,2160)
Var@_FillValue=-9.
Var!1="longitude"
Var!0="latitude"
Var&longitude=lon
Var&latitude=lat
Var&latitude@units="degrees_north"
Var&longitude@units="degrees_east"
;Var1 = Var(latitude|:,longitude|:) 
    wks = gsn_open_wks("png","/home/L.r02229011/fig/irramount")      ; open a wks
    res                = True               ; plot mods desired
    res@gsnDraw   = False                             ; don't draw yet
    res@gsnFrame  = False                             ; don't advance yet
    res@cnFillOn	= True               ; turn on color fill
    res@cnLinesOn	= False              ; turn off contour lines
    res@gsnMaximize	= True
;    res@gsnSpreadColors       = True               ; use full range of color map
;    res@mpProjection = "Robinson"       
    res@mpOutlineBoundarySets       = "National"
    res@mpDataSetName = "Earth..4"
    res@mpCountyLineThicknessF=2.0
    res@mpGeophysicalLineThicknessF =5.0
    res@lbLabelFontHeightF=.02

    res@mpDataBaseVersion   = "MediumRes"
	res@mpFillAreaSpecifiers = (/"water",       "land" /)
	res@mpSpecifiedFillColors  = (/"DeepSkyBlue","gray"/)
    res@mpMaskAreaSpecifiers ="Saudi Arabia"
    res@mpFillDrawOrder             = "PostDraw"
    res@mpFillOn                    = True

	res@mpProjection="LambertConformal"
	res@mpLambertParallel1F = 30.0         ; two parallels
	res@mpLambertParallel2F = 60.0
	res@mpLambertMeridianF  = 40.0        ; central meridian
	res@mpLimitMode         = "Corners"
	res@mpLeftCornerLatF           =   14.6026     ; map area
	res@mpLeftCornerLonF           = 32.0755       ; and
	res@mpRightCornerLatF           = 36.5432       ; latitudes
	res@mpRightCornerLonF           = 60.1822        ; longitudes

	res@mpDataBaseVersion="MediumRes"
	res@mpGridAndLimbOn=True
	res@mpGridLineThicknessF        = 0.5
	res@mpGridSpacingF              = 5
	res@mpLimbLineColor             = "Gray"
	res@mpLimbLineThicknessF        = 0.5
	res@mpNationalLineColor         = "Gray"
	res@mpNationalLineThicknessF    = 0.5
	res@mpPerimLineColor            = "Gray"
	res@mpPerimOn                   = True
	res@mpUSStateLineColor          = "Gray"
	res@mpUSStateLineThicknessF     = 0.5
	res@pmTickMarkDisplayMode       = "Always"
;res@mpPerimOn            = False
;res@mpGridAndLimbOn   = True
;res@mpGridLatSpacingF = 30.
;res@mpGridLonSpacingF = 30.
;res@mpProjection = "Robinson"
;res@mpCenterLonF=150

  res@cnFillMode           = "RasterFill"
;  res@cnFillMode="CellFill"
    res@cnLevelSelectionMode ="ManualLevels"
    res@cnMaxLevelValF  = 30
    res@cnMinLevelValF  = 1
    res@cnLevelSpacingF = 3
;res@cnLevelSelectionMode="ExplicitLevels"
;res@cnLevels=(/1,2,3,4,5,10,15,20,25,50,100,150/)
;res@cnLevels=(/1,2,3,4,5,10,15,20,25,50,100,150/)
;res@cnLevels=(/1,3,5,10,15,20,25,30,35,40,45,50,100,150,200,250,300,400,500,1000/)

    res@cnFillPalette = "precip3_16lev"
;    res@mpMinLatF       = 0
;    res@mpMaxLatF       = 60
;    res@mpMinLonF       = 60 
;    res@mpMaxLonF       = 120
;    res@mpMinLatF       = 0
;    res@mpMaxLatF       = 50
;    res@mpMinLonF       = 20
;    res@mpMaxLonF       = 70
    res@gsnLeftString=varname
    res@gsnAddCyclic=False
;    res@trGridType="TriangularMesh"
printVarSummary(Var&latitude)
    plot=gsn_csm_contour_map(wks,Var,res)

  pmres = True
  pmres@gsMarkerColor = "Black"
  pmres@gsMarkerIndex = 16
  pmres@gsMarkerSizeF = 0.01
;   plotstn1=gsn_add_polymarker(wks,plot,41.69,27.44,pmres)
;   plotstn2=gsn_add_polymarker(wks,plot,43.77,26.30,pmres)
;   plotstn3=gsn_add_polymarker(wks,plot,46.73,24.71,pmres)

          draw(plot)
          frame(wks)
end
