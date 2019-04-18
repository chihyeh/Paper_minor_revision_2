import ROOT
import sys
from ROOT import TFile, TH1F, gDirectory, TCanvas, TPad, TProfile,TGraph, TGraphAsymmErrors,TMultiGraph,TText,TNamed, TLatex
from ROOT import TH1D, TH1, TH1I
from ROOT import gStyle
from ROOT import gROOT
from ROOT import TStyle
from ROOT import TLegend
from ROOT import TMath
from ROOT import TPaveText
from ROOT import TLatex
from array import array
detector_size_array=("r009","r010","r012")
energy_array=("f",[5,10,20,40])
variable_array=("mass_mmdt","mass_sdb2")
#variable_array=("tau21","tau32","c2b1")
#variable_array=("tau21b0b0_ww","tau32b0b0_tt","tau21b2b0_ww","tau32b2b0_tt","tau21b2b2_ww","tau32b2b2_tt","c2b1_b0_ww","c2b1_b2_ww")
#variable_array=("c2b1","c2b1_5","c2b1_7","c2b2")
#width_array=("f",[40,40,40,40])
signal_we_want=("tt","ww")
#for j in range(0,2):
for k in range(0,2):
    for d in range(0,2):
        for i in range(0,4):
            if(variable_array[k]=="mass_sdb2"):
                if(signal_we_want[d]=="tt"):
                    if(energy_array[1][i]<20):
                        f1 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_ttbarrfull010_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_sdb2_1200_no_UOF.root", 'r')
                        f2 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_ttbarrfull009_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_sdb2_1200_no_UOF.root", 'r')
                        f3 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_ttbarrfull012_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_sdb2_1200_no_UOF.root", 'r')
                    if(energy_array[1][i]>=20):
                        f1 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_ttbarrfull010_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_sdb2_2400_no_UOF.root", 'r')
                        f2 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_ttbarrfull009_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_sdb2_2400_no_UOF.root", 'r')
                        f3 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_ttbarrfull012_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_sdb2_2400_no_UOF.root", 'r')
                if(signal_we_want[d]=="ww"):
                    if(energy_array[1][i]<20):
                        f1 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_wwrfull010_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_sdb2_800_no_UOF.root", 'r')
                        f2 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_wwrfull009_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_sdb2_800_no_UOF.root", 'r')
                        f3 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_wwrfull012_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_sdb2_800_no_UOF.root", 'r')
                    if(energy_array[1][i]>=20):
                        f1 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_wwrfull010_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_sdb2_1600_no_UOF.root", 'r')
                        f2 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_wwrfull009_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_sdb2_1600_no_UOF.root", 'r')
                        f3 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_wwrfull012_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_sdb2_1600_no_UOF.root", 'r')
            if(variable_array[k]=="mass_mmdt"):
                if(signal_we_want[d]=="tt"):
                    f1 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_ttbarrfull010_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_mmdt_1200_no_UOF.root", 'r')
                    f2 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_ttbarrfull009_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_mmdt_1200_no_UOF.root", 'r')
                    f3 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_ttbarrfull012_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_mmdt_1200_no_UOF.root", 'r')
                if(signal_we_want[d]=="ww"):
                    f1 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_wwrfull010_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_mmdt_800_no_UOF.root", 'r')
                    f2 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_wwrfull009_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_mmdt_800_no_UOF.root", 'r')
                    f3 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev"+str(energy_array[1][i])+"mumu_pythia6_zprime"+str(energy_array[1][i])+"tev_wwrfull012_onlyhadronic/radius0.4_jetsubstructure_tcalo_for_mmdt_800_no_UOF.root", 'r')
#-----------------------------
            h1 = f1.Get("h_"+variable_array[k])
            numbin_1=h1.GetXaxis().GetNbins()
            for p in range(1,numbin_1):
                if (h1.Integral(1,p)<(h1.Integral(1,numbin_1)/2)<h1.Integral(1,p+1)):
                    break
            central_energy_1=(p+1)*5
            print str(central_energy_1)

            h2 = f2.Get("h_"+variable_array[k])
            numbin_2=h2.GetXaxis().GetNbins()
            for q in range(1,numbin_2):
                if (h2.Integral(1,q)<(h2.Integral(1,numbin_2)/2)<h2.Integral(1,q+1)):
                    break
            central_energy_2=(q+1)*5
            print str(central_energy_2)

            h3 = f3.Get("h_"+variable_array[k])
            numbin_3=h3.GetXaxis().GetNbins()
            for r in range(1,numbin_3):
                if (h3.Integral(1,r)<(h3.Integral(1,numbin_3)/2)<h3.Integral(1,r+1)):
                    break
            central_energy_3=(r+1)*5
            print str(central_energy_3)
            print str(energy_array[1][i])+'TeV'
            print variable_array[k]
    #-----------------------------
            #print signal_we_want[j]
            #print "variable="+variable_array[k]
            #print detector_size_array[i]
            #print "energy="+str(energy_array[1][j])
            #print "width="+str(width_array[1][i])
            #f1 = ROOT.TFile.Open("/Users/ms08962476/MannWhitneyU/cluster_"+detector_size_array[i]+"_tau21_b1_"+str(energy_array[1][j])+"tev_04_eff_error_no_UOF.root",'r')
            #f1 = ROOT.TFile.Open("/Users/ms08962476/MannWhitneyU/cluster_r010_"+variable_array[k]+"_"+str(energy_array[1][j])+"tev_04_eff_no_UOF.root",'r')
            f4= ROOT.TFile.Open("/Users/ms08962476/github/Study_of_mass_variable/codes/A_Cluster_010_"+variable_array[k]+"_"+str(energy_array[1][i])+"tev_eff_1_central_fix_at_Median_bin_"+str(central_energy_1)+"GeV_"+signal_we_want[d]+"_qq_log_no_UOF.root",'r')
            G4=f4.Get("Graph")
            G4.SetLineStyle(1)
            #f1 = ROOT.TFile.Open("/Users/ms08962476/MannWhitneyU/cluster_r010_mass_mmdt_40tev_eff_1_width_40GeV_fix_tt_no_UOF.root",'r')
            #G1=f1.Get("Graph")
            #f2 = ROOT.TFile.Open("/Users/ms08962476/MannWhitneyU/cluster_"+detector_size_array[i]+"_tau21_b1_5_"+str(energy_array[1][j])+"tev_04_eff_error_no_UOF.root",'r')
            #f2 = ROOT.TFile.Open("/Users/ms08962476/MannWhitneyU/cluster_r009_"+variable_array[k]+"_"+str(energy_array[1][j])+"tev_04_eff_no_UOF.root",'r')
            
            f5 = ROOT.TFile.Open("/Users/ms08962476/github/Study_of_mass_variable/codes/A_Cluster_009_"+variable_array[k]+"_"+str(energy_array[1][i])+"tev_eff_1_central_fix_at_Median_bin_"+str(central_energy_2)+"GeV_"+signal_we_want[d]+"_qq_log_no_UOF.root",'r')
            G5=f5.Get("Graph")
            G5.SetLineStyle(7)
            #f2 = ROOT.TFile.Open("/Users/ms08962476/MannWhitneyU/cluster_r009_mass_mmdt_40tev_eff_1_width_40GeV_fix_tt_no_UOF.root",'r')
            #G2=f2.Get("Graph")
            #f3 = ROOT.TFile.Open("/Users/ms08962476/MannWhitneyU/cluster_"+detector_size_array[i]+"_tau21_b2_"+str(energy_array[1][j])+"tev_04_eff_error_no_UOF.root",'r')
            #f3 = ROOT.TFile.Open("/Users/ms08962476/MannWhitneyU/cluster_r012_"+variable_array[k]+"_"+str(energy_array[1][j])+"tev_04_eff_no_UOF.root",'r')
            f6 = ROOT.TFile.Open("/Users/ms08962476/github/Study_of_mass_variable/codes/A_Cluster_012_"+variable_array[k]+"_"+str(energy_array[1][i])+"tev_eff_1_central_fix_at_Median_bin_"+str(central_energy_3)+"GeV_"+signal_we_want[d]+"_qq_log_no_UOF.root",'r')
            G6=f6.Get("Graph")
            G6.SetLineStyle(10)
            #f3 = ROOT.TFile.Open("/Users/ms08962476/MannWhitneyU/cluster_r012_mass_sdb2_"+str(energy_array[1][j])+"tev_eff_1_width_40GeV_fix_"+signal_we_want[k]+"_no_UOF.root",'r')
            #f3 = ROOT.TFile.Open("/Users/ms08962476/MannWhitneyU/cluster_r012_mass_mmdt_40tev_eff_1_width_40GeV_fix_tt_no_UOF.root",'r')
            #G3=f3.Get("Graph")
            #f4 = ROOT.TFile.Open("/Users/ms08962476/MannWhitneyU/cluster_"+detector_size_array[i]+"_c2b2_"+str(energy_array[1][j])+"tev_04_eff_no_UOF.root",'r')
            #G4=f4.Get("Graph")
            #G4.SetLineStyle(10)
    #f4 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev40mumu_pythia6_zprime40tev_qq%rfull010_onlyhadronic/radius0.4_jetsubstructure_tGEN_nonu_no_UOF.root",'r')
    #G4=f4.Get("h_tau32_b1")
    #f5 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev40mumu_pythia6_zprime40tev_qq%rfull009_onlyhadronic/radius0.4_jetsubstructure_tGEN_nonu_no_UOF.root", 'r')
    #G5=f5.Get("h_tau32_b1")
    #f6 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev40mumu_pythia6_zprime40tev_qq%rfull012_onlyhadronic/radius0.4_jetsubstructure_tGEN_nonu_no_UOF.root", 'r')
    #G6=f6.Get("h_tau32_b1")
    #f2 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev40mumu_pythia6_zprime40tev_qq%rfull012_onlyhadronic/radius0.4_jetsubstructure_tGEN_nonu_no_UOF.root", 'r')
    #G2=f2.Get("h_tau32_b1")
    #f3 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev40mumu_pythia6_zprime40tev_ttbarrfull012_onlyhadronic/radius0.4_jetsubstructure_retcalo_no_UOF.root", 'r')
    #G3=f3.Get("h_tau32_b1")
    #f4 = ROOT.TFile.Open("/Users/ms08962476/FD/VHEPP/analyze/onlyhadron/tev40mumu_pythia6_zprime40tev_qq%rfull012_onlyhadronic/radius0.4_jetsubstructure_retcalo_no_UOF.root", 'r')
    #G4=f4.Get("h_tau32_b1")
    #fixed_point=i
    #f3 = ROOT.TFile.Open(sys.argv[3], 'r')
    #f4 = ROOT.TFile.Open(sys.argv[4], 'r')

    #G1 = f1.Get("Graph")
    #G1.SetName("G1")
    #G2 = f2.Get("Graph")
    #G2.SetName("G2")
    #G3 = f3.Get("Graph")
    #G3.SetName("G3")

    #G1.Sumw2()
    #G2.Sumw2()
    #G3.Sumw2()
    #G4.Sumw2()
    #G5.Sumw2()
    #G6.Sumw2()


    #G1.Scale(1.0/G1.Integral())
    #G2.Scale(1.0/G2.Integral())
    #G3.Scale(1.0/G3.Integral())
    #G4.Scale(1.0/G4.Integral())
    #G5.Scale(1.0/G5.Integral())
    #G6.Scale(1.0/G6.Integral())



            c = TCanvas("c1", "c1",0,0,1000,1000)
            gStyle.SetOptStat(0)
            gStyle.SetTitleSize(0.05,"XY")
            gStyle.SetTitleFont(62,"XY")
            gStyle.SetLegendFont(62)

    #tau21-leg = TLegend(0.1,0.7,0.6,0.9)


            mg=TMultiGraph()

    #G1.Draw("E")
    #G2.Draw("E")
    #G3.Draw("E")
    #G4.Draw("E")
    #G5.Draw("E")
    #G6.Draw("E")


    #G1.Draw("histsame")
    #G2.Draw("histsame")
    #G3.Draw("histsame")
    #G4.Draw("histsameE")
    #G5.Draw("histsameE")
    #G6.Draw("histsameE")


    #G1.SetLineWidth(2)
    #G2.SetLineWidth(2)
    #G3.SetLineWidth(2)
    #G4.SetLineWidth(2)
    #G5.SetLineWidth(2)
    #G6.SetLineWidth(2)


    #G1.SetLineStyle(1)
    #G2.SetLineStyle(1)
    #G3.SetLineStyle(1)
    #G4.SetLineStyle(4)
    #G5.SetLineStyle(4)
    #G6.SetLineStyle(4)

    #G3.Draw("ALPsame")
    #G4.Draw("ALPsame")
    #energy_cut1= 0.25
    #energy_cut2= 0.5
    #fixed_point1=str(fixed_point)
    #energy1_cut=str(energy_cut1)
    #energy2_cut=str(energy_cut2)

            mg.Add(G4)
            mg.Add(G5)
            mg.Add(G6)
            #mg.Add(G4)
    #mg.Add(G4)
    #G1.SetLineColor(1)
    #G2.SetLineColor(2)
    #G3.SetLineColor(3)
    #G4.SetLineColor(2)
    #G5.SetLineColor(1)
    #G6.SetLineColor(3)

    #G1.SetXTitle(variable);
    #tau32,tau21 -> 0.04  c2b1 ->0.01
    #if (variable=="c2b1"):
    #    d=0.01
    #else :
    #    d=0.04
    #d1=str(d)
    #G1.SetYTitle("number of jet per "+d1);
    #G1.SetTitle("Study_of_difference_in_"+variable+"_truth_level_"+energy1+"tev")
    #G1.SetTitle("cluster_"+files+"_"+variable+"_"+energy1+"tev_distribution_tGEN_nonu_vs_detector_level")
    #mg.SetTitle("raw_"+variable+"_"+energy1+"tev_"+energy1_cut+"_compare_to_"+energy2_cut+"GeV_eff; signal efficiency; 1 - background efficiency")
    #mg.SetTitle("cluster_"+variable+"_"+energy1+"tev_eff_fixed_width_to_"+fixed_width1+"GeV_tt_qq ; signal efficiency; 1 - background efficiency")
    #mg.SetTitle("cluster_mass_sdb2_"+str(energy_array[1][j])+"tev_eff_1_width_40GeV_fix_"+signal_we_want[k]+"; signal efficiency; 1 - background efficiency")
            mg.SetTitle(" ; signal efficiency; background rejection")
    #mg.GetXaxis().SetTitleFont(62)
        #mg.GetYaxis().SetTitleFont(62)
            mg.Draw("ALP")
    #mg.GetXaxis().SetLabelOffset(999)
    #mg.GetXaxis().SetLabelize(0)
    #h=min(G1.GetHistogram().GetMinimum(),G2.GetHistogram().GetMinimum(),G3.GetHistogram().GetMinimum())
        #l=max(G1.GetHistogram().GetMaximum(),G2.GetHistogram().GetMaximum(),G3.GetHistogram().GetMaximum())
        #mg.GetXaxis().SetRangeUser(-2,1.1)
            if(signal_we_want[d]=="tt"):
                mg.GetYaxis().SetRangeUser(1,100)#1~80
            if(signal_we_want[d]=="ww"):
                mg.GetYaxis().SetRangeUser(1,80)#1~80
        #-----------------------------------------------#

            mg.GetXaxis().SetLabelSize(0.05)
            mg.GetYaxis().SetLabelSize(0.05)
            mg.GetXaxis().SetLabelFont(60)
            mg.GetYaxis().SetLabelFont(60)
    #G1.GetXaxis().SetRangeUser(0,1)
    #G1.GetYaxis().SetRangeUser(0.73,1.5)
    #G1.GetYaxis().SetRangeUser(0,1.5)


    #t = TText()
    #t.SetTextAlign(20)
    #t.SetTextSize(0.030)
    #t.SetTextFont(60)
    #t.SetTextColor(4)
    #label=["20*20","5*5","1*1"]
    #for i in range(3):
    #    t.DrawText(i+1,-0.03,label[i])

    #leg.AddEntry("","signal:z'->"+signal_we_want[j],"")
    #leg.AddEntry("","background:z'->qq","")

    #leg.AddEntry(G1,"z'->tt(truth-level)","l")
    #leg.AddEntry(G2,"z'->qq(truth-level)","l")
    #leg.AddEntry(G3,"z'->tt(detector-level)","l")
    #leg.AddEntry(G4,"z'->qq(detector-level)","l")
    #leg.AddEntry(G1,"z'->tt(truth-level-20*20)","l")
    #leg.AddEntry(G2,"z'->tt(truth-level-5*5)","l")
    #leg.AddEntry(G3,"z'->tt(truth-level-1*1)","l")
    #leg.AddEntry(G4,"z'->qq(truth-level-20*20)","l")
    #leg.AddEntry(G5,"z'->qq(truth-level-5*5)","l")
    #leg.AddEntry(G6,"z'->qq(truth-level-1*1)","l")
    #leg1=TLegend(0.05,0.3,0.35,0.4)
            #if(variable_array[i]=="c2b1_5"):
            #    leg1.AddEntry("","Z'("+str(energy_array[1][j])+"TeV)#rightarrowW^{+}W^{-}#rightarrow2 jets","")
            #if(variable_array[i]=="c2b1_7"):
            #    leg1.AddEntry("","Z'("+str(energy_array[1][j])+"TeV)#rightarrowW^{+}W^{-}#rightarrow2 jets","")
            #if(variable_array[i]=="c2b2"):
            #leg1.AddEntry("","Z'("+str(energy_array[1][j])+"TeV)#rightarrowt#bar{t}#rightarrow3 jets","")
            if(signal_we_want[d]=="ww"):
                leg1=TLegend(0.5,0.8,0.6,0.9)
                leg1.SetFillColor(0)
                leg1.SetFillStyle(0)
                leg1.SetTextSize(0.05)
                leg1.SetBorderSize(0)
                leg1.SetTextFont(22)
                leg1.AddEntry("","Z'#rightarrowW^{+}W^{-}#rightarrow2 jets","")
            #if(variable_array[i]=="c2b1"):
            if(signal_we_want[d]=="tt"):
                leg1=TLegend(0.55,0.8,0.65,0.9)
                leg1.SetFillColor(0)
                leg1.SetFillStyle(0)
                leg1.SetTextSize(0.05)
                leg1.SetBorderSize(0)
                leg1.SetTextFont(22)
                leg1.AddEntry("","Z'#rightarrowt#bar{t}#rightarrow2 jets","")
            
            
            leg=TLegend(0.5,0.6,0.95,0.8)
            #leg = TLegend(0.1,0.1,0.5,0.3)
            leg.SetFillColor(0)
            leg.SetFillStyle(0)
            leg.SetTextSize(0.05)
            leg.SetTextFont(22)
            leg.SetBorderSize(0)
            leg.AddEntry(G4,"20#times20 cm^{2} HCAL","l")
            leg.AddEntry(G5,"5#times5 cm^{2} HCAL","l")
            leg.AddEntry(G6,"1#times1 cm^{2} HCAL","l")
            
            
            #leg.AddEntry(G1,"#tau_{21} #beta=1","l")
            #leg.AddEntry(G2,"#tau_{21} #beta=1.5","l")
            #leg.AddEntry(G3,"#tau_{21} #beta=2","l")

            
        


    #        leg.AddEntry(G1,"c_{(2)}^{1}","l")
    #        leg.AddEntry(G2,"c_{(2)}^{1.5}","l")
    #        leg.AddEntry(G3,"c_{(2)}^{1.7}","l")
    #        leg.AddEntry(G4,"c_{(2)}^{2}","l")

    #leg.AddEntry("G4","#sqrt{s}=40TeV","l")

            c.Draw()
            c.Update()
            c.SetLogy()
            leg.Draw()
            leg1.Draw()
            #        c.Print("cluster_"+detector_size_array[i]+"_c_variable_"+str(energy_array[1][j])+"tev_04_eff.eps")
    #c.Print("cluster_"+detector_size_array[i]+"_c_variable_"+str(energy_array[1][j])+"tev_04_eff.eps")
    #c.Print("cluster_"+detector_size_array[i]+"_tau21_compare_different_beta_"+str(energy_array[1][j])+"tev.pdf")
    #       c.Print("cluster_"+detector_size_array[i]+"_tau21_compare_different_beta_"+str(energy_array[1][j])+"tev.eps")
            c.Print("A_Cluster_"+variable_array[k]+"_"+str(energy_array[1][i])+"tev_eff_1_central_fix_at_Median_bin_"+signal_we_want[d]+"_qq_log_no_UOF.eps")
    #c.Print("cluster_mass_sdb2_"+str(energy_array[1][j])+"tev_eff_fixed_width_to_40GeV_"+signal_we_want[k]+"_qq.eps")
    #c.Print("cluster_mass_sdb2_"+str(energy_array[1][j])+"tev_eff_fixed_width_to_40GeV_"+signal_we_want[k]+"_qq.pdf")
    #c.Print("cluster_"+variable_array[k]+"_c_variable_"+str(energy_array[1][j])+"tev_04_eff_error.pdf")
#c.Print("cluster_"+variable_array[k]+"_c_variable_"+str(energy_array[1][j])+"tev_04_eff_error.eps")
#c.Print("cluster_"+variable+"_"+str(energy_array[1][i])+"tev_eff_fixed_width_to_"+str(width_array[1][i])+"GeV_"+signal_we_want[j]+"_qq.pdf")
#c.Print("cluster_"+variable+"_"+energy1+"tev_eff_fixed_width_to_"+fixed_width1+"GeV_tt_qq.pdf")
#c.Print("Study_of_difference_in_"+variable+"_truth_level_"+energy1+"tev.pdf")
#c.Print("cluster_"+files+"_"+variable+"_"+energy1+"tev_distribution_tGEN_nonu_vs_detector_level.pdf")
#c.Print("raw_"+variable+"_"+energy1+"tev_"+energy1_cut+"_compare_to_"+energy2_cut+"GeV_eff.pdf")




